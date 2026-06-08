import random
import time

def criar_tabuleiro(agua):
    return [[agua] * 5 for _ in range(5)]

def posicionar_pecas(tabuleiro, navio, lista_num):
    while True:
        linha = input("Digite em qual linha deseja posicionar seu navio: ")

        if not linha.isdigit():
            print("Digite apenas números!")
        elif int(linha) not in lista_num:
            print("Linha fora dos limites! Digite entre 0 e 4.")
        else:
            while True:
                coluna = input("Digite em qual coluna deseja posicionar seu navio: ")

                if not coluna.isdigit():
                    print("Digite apenas números!")
                elif int(coluna) not in lista_num:
                    print("Coluna fora dos limites! Digite entre 0 e 4.")
                elif tabuleiro[int(linha)][int(coluna)] == "N":
                    print("Posição ocupada! Selecione outro lugar.")
                else:
                    tabuleiro[int(linha)][int(coluna)] =navio 
                    print("Posição ocupada com sucesso!")
                    break
            break

def posicionar_pecas_ia(tabuleiro, navio, lista_num):
    while True:
        linha = random.choice(lista_num)
        coluna = random.choice(lista_num)

        if tabuleiro[linha][coluna] != "N":
            tabuleiro[linha][coluna] = navio
            break

def mostrar_tabuleiros(tabuleiro, tabuleiroIa):
    print("Seu tabuleiro")
    for linha in tabuleiro:
        print(linha)

    print("Tabuleiro da IA")
    for linha in tabuleiroIa:
        print(linha)

def atacar(tabuleiro_verdadeiro, tabuleiro_visivel, linha, coluna, navio, acerto, erro):
    if tabuleiro_verdadeiro[linha][coluna] == navio:
        tabuleiro_verdadeiro[linha][coluna] = acerto
        tabuleiro_visivel[linha][coluna] = acerto
        print("Acertou um navio!")
    else:
        tabuleiro_verdadeiro[linha][coluna] = erro
        tabuleiro_visivel[linha][coluna] = erro
        print("Errou!")

def ataque_jogador(tabuleiroIaVerdadeiro, tabuleiroIa, lista_num, navio, acerto, erro):
    print("Sua vez de atacar!")
    while True:
        linha = input("Digite a linha para atacar: ")
        if not linha.isdigit():
            print("Digite apenas números!")
        elif int(linha) not in lista_num:
            print("Linha fora dos limites! Digite entre 0 e 4.")
        else:
            while True:
                coluna = input("Digite a coluna para atacar: ")
                if not coluna.isdigit():
                    print("Digite apenas números!")
                elif int(coluna) not in lista_num:
                    print("Coluna fora dos limites! Digite entre 0 e 4.")
                elif tabuleiroIaVerdadeiro[int(linha)][int(coluna)] == acerto or tabuleiroIaVerdadeiro[int(linha)][int(coluna)] == erro:
                    print("Você já atacou essa posição! Escolha outra.")
                else:
                    atacar(tabuleiroIaVerdadeiro, tabuleiroIa, int(linha), int(coluna), navio, acerto, erro)
                    break
            break
    
def ataque_ia(tabuleiro, lista_num, navio, acerto, erro):
    print("Vez da IA atacar!")
    while True:
        linha = random.choice(lista_num)
        coluna = random.choice(lista_num)
        if tabuleiro[linha][coluna] != acerto and tabuleiro[linha][coluna] != erro:
            atacar(tabuleiro, tabuleiro, linha, coluna, navio, acerto, erro)
            break

def verificar_vitoria(tabuleiro, navio):
    for linha in tabuleiro:
        if navio in linha:
            return False
        else:
            return True



def main():
    agua = "#"
    navio = "N"
    acerto = "X"
    erro = "O"
    lista_num = [0,1,2,3,4]

    tabuleiro = criar_tabuleiro(agua)
    tabuleiroIa = criar_tabuleiro(agua)
    tabuleiroIaVerdadeiro = criar_tabuleiro(agua)

    print("Posicione seus 5 navios")
    for i in range(5):
        print(f"Navio {i+1}:")
        posicionar_pecas(tabuleiro, navio, lista_num)

    for i in range(5):
        posicionar_pecas_ia(tabuleiroIaVerdadeiro, navio, lista_num)

    print("Jogo iniciado!")
    while True:
        mostrar_tabuleiros(tabuleiro, tabuleiroIa)
        ataque_jogador(tabuleiroIaVerdadeiro, tabuleiroIa, lista_num, navio, acerto, erro)
        if verificar_vitoria(tabuleiroIaVerdadeiro, navio):
            mostrar_tabuleiros(tabuleiro, tabuleiroIa)
            print("Parabéns! Você venceu!")
            break

        ataque_ia(tabuleiro, lista_num, navio, acerto, erro)
        if verificar_vitoria(tabuleiro, navio):
            mostrar_tabuleiros(tabuleiro, tabuleiroIa)
            print("A IA venceu! Tente novamente.")
            break

main()