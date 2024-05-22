import math

def distancia(P1, P2):
    absc = P1[0] - P2[0]
    orde = P1[1] - P2[1]
    dist = math.sqrt(absc**2 + orde**2)

    return dist 
    #Calcula a distância entre dois pontos fornecidos P1=[x1, y1] e P2 = [x2, y2]

def aceleracaoGravitacional(Astro, P):
    

    return   
    #Calcula e devolve a aceleração da atração gravitacional [ax, ay] exercida sobre a nave no ponto P = [x,y] pelo astro Astro
def aceleracaoResultante(Astro, P):

    return
    #Calcula e devolve a aceleração resultante [ax, ay] da soma das contribuições exercidas por cada um dos astros presentes na lista Astros sobre a nave no ponto P=[x,y]
def deteccaoColisao(Nave, Astros):

    return
    #Verifica se ocorre sobreposição entre a nave fornecida com algum dos astros presentes na lista Astros. Devolve True se a nmave colidiu com algum astro, caso contrário a função retorna False
def atualizaNave(Nave, Astros, delta_t):

    return 
    #Atualiza a posição e velocidade da nave em Nave sujeita às forças de atração gravitacional dos astros presentes na lista Astros, após um intervalo de tempo delta_t
def distanciaAstroMaisProximo(Nave, Astros):
    
    return
    #Calcula a distância da nave 𝑁 𝑎𝑣 𝑒 em relação ao astro mais próximo dentre os astros presentes na lista 𝐴𝑠𝑡𝑟𝑜𝑠. A distância deve ser medida em relação a superfície do astro e da nave. Em caso de nave colidida, a distância deve ser zero.
def simulacao(Naves, Astros, niter, delta_t):

    return
    #muito grande

iter = int(input("Número máximo de iterações: "))
delta_t = int(input("Delta t: "))
n = int(input("Número de naves: "))
Naves = []
Astros = []

for i in range(n):
    print("*** Nave", i+1, "***")
    Naves.append(input("Digite a posição (x,y): ").split()) 
    Naves.append(input("Digite a velocidade incial (vx, vy): ").split())
    Naves.append(input("Digite o raio: "))
a = int(input("Número de astros: "))
for j in range(a):
    print("*** Astro", j+1, "***")
    Astros.append(input("Digite a posição (x,y): ").split())
    Astros.append(input("Digite a massa: "))
    Astros.append(input("Digite o raio: "))

print(Naves, end=" ")
print(Astros)



    
