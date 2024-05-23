def no_minas_em(campo:list, linha:int, coluna:int) -> int:
    ''' 
    Recebe uma matriz de 0s (= posições vazias) e 1s (= minas), uma linha
    e uma coluna e retorna o número de minas existentes ao redor daquela
    coordenada ou -1 caso exista uma mina naquela coordenada.
    '''
    soma_minas = 0
    if campo[linha][coluna] == -1:
        soma_minas = -1
        return soma_minas
    if linha >=1 and linha<len(campo)-1 and coluna >=1 and coluna<len(campo[0])-1:
        for l in range(linha-1, linha+2, 1):
            for c in range(coluna-1, coluna+2, 1):
                if campo[l][c] == -1:
                    soma_minas+=1
    elif linha == 0 and coluna != 0:
        for l in range(linha, linha+2, 1):
            for c in range(coluna-1, coluna+2, 1):
                if campo[l][c] == -1:
                    soma_minas+=1
    elif linha != 0 and coluna == 0:
        for l in range(linha-1, linha+2, 1):
            for c in range(coluna, coluna+2, 1):
                if campo[l][c] == -1:
                    soma_minas+=1
    elif linha == len(campo)-1 and coluna != len(campo[0])-1:
        for l in range(linha-1, linha+1, 1):
            for c in range(coluna-1, coluna+2, 1):
                if campo[l][c] == -1:
                    soma_minas+=1
    elif linha != len(campo)-1 and coluna == len(campo[0])-1:
        for l in range(linha-1, linha+1, 1):
            for c in range(coluna-1, coluna+1, 1):
                if campo[l][c] == -1:
                    soma_minas+=1
    elif linha == 0 and coluna == 0:
        for l in range(linha, linha+2, 1):
            for c in range(coluna, coluna+2, 1):
                if campo[l][c] == -1:
                    soma_minas+=1
    elif linha == len(campo)-1 and coluna == 0:
        for l in range(linha-1, linha+1, 1):
            for c in range(coluna, coluna+2, 1):
                if campo[l][c] == -1:
                    soma_minas+=1
    elif linha == len(campo)-1 and coluna == len(campo[0])-1:
        for l in range(linha-1, linha+1, 1):
            for c in range(coluna-1, coluna+1, 1):
                if campo[l][c] == -1:
                    soma_minas+=1
    elif linha == 0 and coluna == len(campo[0])-1:
        for l in range(linha, linha+2, 1):
            for c in range(coluna-1, coluna+1, 1):
                if campo[l][c] == -1:
                    soma_minas+=1
    return soma_minas

    # TERMINAR


def main():
    '''
    Programa que lê uma matriz 0s (= posições vazias) e 1s (= minas), uma
    coordenada e imprime quantas minas existem ao redor daquela coordenada.
    '''
    # A = [[ 0, -1, 0, -1, -1,  0, -1],
    #      [ 0, 0,  0,  0, -1,  0, -1],
    #      [-1, 0, -1, -1, -1,  0,  0],
    #      [-1, 0, -1,  0,  0,  0, -1],
    #      [ 0, 0, -1,  0,  0, -1, -1]]    
    # Comente a linha abaixo e descomente as alinhas acima para testar
    # com a matriz do exemplo do enunciado.
    # Lembre-se de desverter as alteracoes para a avaliacao.

    A = leiamatriz()

    lin = int(input("Entre com a linha desejada: "))
    col = int(input("Entre com a coluna desejada: "))
    minas = no_minas_em(A, lin, col)
    print(f"O número de minas ao redor de ({lin}, {col}) é: {minas}")


# NAO MODIFICAR TRECHO ABAIXO
def leiamatriz() -> list:
    ''' 
    Função que lê do teclado o número nlinhas de linhas
    e o número ncolunas de colunas e os elementos de
    uma matriz de dimensão nlinhas x ncolunas.
    A função cria e retorna a matriz lida.
    '''
    nlinhas  = int(input("Número de linhas: "))
    ncolunas = int(input("Número de colunas: "))
    matriz = []
    for i in range(nlinhas):
        linha = []
        for j in range(ncolunas):
            elemento = int(input(f"Elemento em {i},{j}: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

if __name__ == '__main__':
    main()
