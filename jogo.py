import random


def criar_tabuleiro(agua):
    return [[agua] * 10 for _ in range(10)]

def posicionar_peças(tabuleiro,linha,coluna,navio):
    for i in range(10):
        l = linha
        c = coluna
        tabuleiro[l][c] = navio




def main():
    agua = "#"
    navio = "N"
    acerto = "X"
    erro = "0"
    lista_num = [0,1,2,3,4,5,6,7,8,9]


    tabuleiro = criar_tabuleiro(agua) 
    tabuleiroIa = criar_tabuleiro(agua)

    for i in range(5):
        linha = int(input("Digite em qual linha deseja posicionar seu navio: "))
        coluna = int(input("Digite em qual coluna deseja posicionar seu navio: "))
        posicionar_peças(tabuleiro,linha,coluna,navio)
    
    for i in range(5):
        linha = random.choice(lista_num)
        coluna = random.choice(lista_num)
        posicionar_peças(tabuleiroIa,linha,coluna,navio)


    for linha in tabuleiro:
        print(linha)
    print()
    print()
    print()
    print()
    print()
    for linha in tabuleiroIa:
        print(linha)


main()