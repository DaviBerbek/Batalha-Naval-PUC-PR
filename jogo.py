import random

def criar_tabuleiro(agua):
    return [[agua] * 10 for _ in range(10)]

def posicionar_pecas(tabuleiro, navio, lista_num):
    while True:
        linha = input("Digite em qual linha deseja posicionar seu navio: ")

        if not linha.isdigit():
            print("Digite apenas números!")
        elif int(linha) not in lista_num:
            print("Linha fora dos limites! Digite entre 0 e 9.")
        else:
            while True:
                coluna = input("Digite em qual coluna deseja posicionar seu navio: ")

                if not coluna.isdigit():
                    print("Digite apenas números!")
                elif int(coluna) not in lista_num:
                    print("Coluna fora dos limites! Digite entre 0 e 9.")
                elif tabuleiro[int(linha)][int(coluna)] == "N":
                    print("Posição ocupada! Selecione outro lugar.")
                else:
                    tabuleiro[int(linha)][int(coluna)] = navio
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
    print("\n--- Seu tabuleiro ---")
    for linha in tabuleiro:
        print(linha)

    print("\n--- Tabuleiro da IA ---")
    for linha in tabuleiroIa:
        print(linha)

def main():
    agua = "#"
    navio = "N"
    lista_num = [0,1,2,3,4,5,6,7,8,9]

    tabuleiro = criar_tabuleiro(agua)
    tabuleiroIa = criar_tabuleiro(agua)
    tabuleiroIaVerdadeiro = criar_tabuleiro(agua)

    print("=== Posicione seus 5 navios ===")
    for i in range(5):
        print(f"\nNavio {i+1}:")
        posicionar_pecas(tabuleiro, navio, lista_num)

    for i in range(5):
        posicionar_pecas_ia(tabuleiroIaVerdadeiro, navio, lista_num)

    mostrar_tabuleiros(tabuleiro, tabuleiroIa)

main()