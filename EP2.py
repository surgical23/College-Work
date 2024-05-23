from math import sqrt,pow

def distancia(P1, P2):
    x = P1[0] - P2[0]
    y = P1[1] - P2[1]
    P = sqrt(x**2 + y**2)

    return P
    #Calcula a distância entre dois pontos fornecidos P1=[x1, y1] e P2 = [x2, y2]

def aceleracaoGravitacional(Astro, P):
    a=[]
    a.append(8.65*pow(10, -13)*Astro[1]/(distancia(P, Astro[0])**3)*(-P[0]+Astro[0][0]))
    a.append(8.65*pow(10, -13)*Astro[1]/(distancia(P, Astro[0])**3)*(-P[1]+Astro[0][1]))
    

    return a
    #Calcula e devolve a aceleração da atração gravitacional [ax, ay] exercida sobre a nave no ponto P = [x,y] pelo astro Astro
def aceleracaoResultante(Astro, P):
    ar = [0,0]
    for j in range(len(Astro)):
        a_j = aceleracaoGravitacional(Astro[j], P)
        ar[0]+= a_j[0]
        ar[1]+=a_j[1]

    return ar
    #Calcula e devolve a aceleração resultante [ax, ay] da soma das contribuições exercidas por cada um dos astros presentes na lista 
    #Astros sobre a nave no ponto P=[x,y]
def deteccaoColisao(Nave, Astros):
    colisao = False
    pos_nave = Nave[0]
    raio_nave = Nave[2]

    for Astro in Astros:
        colis = distancia(Astro[0], pos_nave) - Astro[2] - raio_nave
        if colis <= 0:
            colisao = True
    return colisao
    #Verifica se ocorre sobreposição entre a nave fornecida com algum dos astros presentes na lista Astros. 
    #Devolve True se a nave colidiu com algum astro, caso contrário a função retorna False
def atualizaNave(Nave, Astros, delta_t):
    Posicao = []
    Velocidade =[]
    [ax, ay] = aceleracaoResultante(Astros, Nave[0])
    Velocidade.append(ax*delta_t + Nave[1][0])
    Velocidade.append(ay*delta_t+Nave[1][1])
    Posicao.append(Nave[0][0]+Velocidade[0]*delta_t-ax*delta_t**2/2)
    Posicao.append(Nave[0][1]+Velocidade[1]*delta_t-ay*delta_t**2/2)
    Nave[0] = Posicao
    Nave[1] = Velocidade
    #Atualiza a posição e velocidade da nave em Nave sujeita às forças de atração gravitacional dos astros presentes na lista Astros, 
    #após um intervalo de tempo delta_t
def distanciaAstroMaisProximo(Nave, Astros):
    colis = float("inf")
    pos_nave = Nave[0]
    raio_nave = Nave[2]

    for Astro in Astros:
        colis = min(colis, distancia(Astro[0], pos_nave) - Astro[2] - raio_nave)
            
    return max(colis, 0)
    #Calcula a distância da nave Nave em relação ao astro mais próximo dentre os astros presentes na lista 𝐴𝑠𝑡𝑟𝑜𝑠. 
    #A distância deve ser medida em relação a superfície do astro e da nave. Em caso de nave colidida, a distância deve ser zero.
def simulacao(Naves, Astros, niter, delta_t):
    listaT = []
    listaD = []
    for Nave in Naves:
        d = []
        t = []
        for i in range(niter):
            if not deteccaoColisao(Nave, Astros):
                atualizaNave(Nave, Astros, delta_t)
            d.append(distanciaAstroMaisProximo(Nave, Astros))
            t.append(Nave[0])

        listaT.append(t)
        listaD.append(d)

    return listaT, listaD
def main():
    niter = int(input("Número máximo de iterações: "))    
    delta_t = float(input("Delta t: "))
    nnaves = int(input("Número de naves: "))
    Naves = []
    for i in range(nnaves):
        print("*** Nave %d ***"%(i+1))
        x,y = input("Digite a posição (x,y): ").split()
        x,y = float(x),float(y)
        vx,vy = input("Digite a velocidade inicial (vx,vy): ").split()
        vx,vy = float(vx),float(vy)
        r = float(input("Digite o raio: "))
        Naves.append([[x,y], [vx,vy], r])

    nastros = int(input("Número de astros: "))
    Astros = []
    for i in range(nastros):
        print("*** Astro %d ***"%(i+1))
        x,y = input("Digite a posição (x,y): ").split()
        x,y = float(x),float(y)
        massa = float(input("Digite a massa: "))
        R = float(input("Digite o raio: "))        
        Astros.append([[x,y], massa, R])

    T, D = simulacao(Naves, Astros, niter, delta_t)
    for i in range(niter):
        print("********* iteração %d *********"%(i+1))
        for j in range(nnaves):
            print("*** Nave %d ***"%(j+1))
            print("Posição: ",end="")
            P = T[j][i]
            print("(%.3f,%.3f)"%(P[0],P[1]))
            print("Distância ao astro mais próximo: ",end="")
            print("%.3f"%(D[j][i]))


if __name__ == "__main__":
    main()
