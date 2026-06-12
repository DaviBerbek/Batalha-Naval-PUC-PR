import random
import time

def criar_tabuleiro(agua):
    return [[agua] * 10 for _ in range(5)] # aumento do tabuleiro

def posicionar_pecas(tabuleiro, navio, lista_linhas, lista_colunas):
    while True:
        linha = input("Digite em qual linha deseja posicionar seu navio (Linhas de 1 a 5): ") # +info

        if not linha.isdigit():
            print("Digite apenas números!")
        elif int(linha) - 1 not in lista_linhas:
            print("Linha fora dos limites! Digite entre 1 e 5.")
        else:
            while True:
                coluna = input("Digite em qual coluna deseja posicionar seu navio (Colunas de 1 a 10): ") # +info

                if not coluna.isdigit():
                    print()
                    print("Digite apenas números!")
                    print()
                elif int(coluna) - 1 not in lista_colunas:
                    print()
                    print("Coluna fora dos limites! Digite entre 1 e 10.")
                    print()
                elif tabuleiro[int(linha) - 1][int(coluna) - 1] == "N":
                    print()
                    print("Posição ocupada! Selecione outro lugar.")
                    print()
                else:
                    tabuleiro[int(linha) - 1][int(coluna) - 1] =navio
                    print()
                    print("Posição ocupada com sucesso!")
                    print()
                    break
            break

def posicionar_pecas_ia(tabuleiro, navio, lista_linhas, lista_colunas):
    while True:
        linha = random.choice(lista_linhas) # famosas linhas e colunas
        coluna = random.choice(lista_colunas)

        if tabuleiro[linha][coluna] != "N":
            tabuleiro[linha][coluna] = navio
            break

# contar os navios restantes, melhoria no feedback (usado dentro de mostrar_tabuleiros)
def contar_navios(tabuleiro, navio):
    total = 0
    for linha in tabuleiro:
        total += linha.count(navio)
    return total

# melhoria na visualização (normal usa aspas, virgula e aquela coisa toda)
def renderizar_tabuleiro(titulo, tabuleiro):
    print(f"\n{titulo}")
    print("   " + " ".join(str(i+1) for i in range(len(tabuleiro[0]))))
    for i, linha in enumerate(tabuleiro):
        print(f"{i+1} {' '.join(linha)}")



def mostrar_tabuleiros(tabuleiro, tabuleiroIa, tabuleiroIaVerdadeiro, navio):
    # FUNCIONA, aqui alterei só para tirar a visualização base
    # print("Seu tabuleiro")
    # for linha in tabuleiro:
    #     print(linha)

    # print("Tabuleiro da IA")
    # for linha in tabuleiroIa:
    #     print(linha)
    seus_navios = contar_navios(tabuleiro, navio)
    navios_ia = contar_navios(tabuleiroIaVerdadeiro, navio)

    print("\nLegenda: # = Água | N = Navio | X = Acerto | O = Erro") # Leggendaaa
    time.sleep(1)
    print(f"\nSeus navios restantes: {seus_navios}/5")
    time.sleep(1)
    print(f"Navios da IA restantes: {navios_ia}/5")
    time.sleep(1)

    renderizar_tabuleiro("Seu tabuleiro", tabuleiro)
    time.sleep(1)
    renderizar_tabuleiro("Tabuleiro da IA", tabuleiroIa)
    time.sleep(1)



def atacar(tabuleiro_verdadeiro, tabuleiro_visivel, linha, coluna, navio, acerto, erro):
    if tabuleiro_verdadeiro[linha][coluna] == navio:
        tabuleiro_verdadeiro[linha][coluna] = acerto
        tabuleiro_visivel[linha][coluna] = acerto
        time.sleep(1)
        print("Acertou um navio!")
    else:
        tabuleiro_verdadeiro[linha][coluna] = erro
        tabuleiro_visivel[linha][coluna] = erro
        time.sleep(1)
        print("Errou!")

def ataque_jogador(tabuleiroIaVerdadeiro, tabuleiroIa, lista_linhas, lista_colunas, navio, acerto, erro):
    print("Sua vez de atacar!")
    while True:
        linha = input("Digite a linha para atacar (1 - 5): ") # +info
        if not linha.isdigit():
            print("Digite apenas números!")
        elif int(linha) - 1 not in lista_linhas:
            print("Linha fora dos limites! Digite entre 1 e 5.")
        else:
            while True:
                coluna = input("Digite a coluna para atacar (1 - 10): ") # +info
                if not coluna.isdigit():
                    print("Digite apenas números!")
                elif int(coluna) - 1 not in lista_colunas:
                    print("Coluna fora dos limites! Digite entre 1 e 10.")
                elif tabuleiroIaVerdadeiro[int(linha) - 1][int(coluna) - 1] == acerto or tabuleiroIaVerdadeiro[int(linha) - 1][int(coluna) - 1] == erro:
                    print("Você já atacou essa posição! Escolha outra.")
                else:
                    atacar(tabuleiroIaVerdadeiro, tabuleiroIa, int(linha) - 1, int(coluna) - 1, navio, acerto, erro)
                    break
            break

def ataque_ia(tabuleiro, lista_linhas, lista_colunas, navio, acerto, erro):
    print("Vez da IA atacar!")
    while True:
        linha = random.choice(lista_linhas) # linha e coluna de cria
        coluna = random.choice(lista_colunas)
        if tabuleiro[linha][coluna] != acerto and tabuleiro[linha][coluna] != erro:
            atacar(tabuleiro, tabuleiro, linha, coluna, navio, acerto, erro)
            break

# Primeira iteração que não achar no navio já delara a vitória. Agora só declara a vitória se passar por todas as linhas e não encontrar nenhum navio.
def verificar_vitoria(tabuleiro, navio):
    for linha in tabuleiro:
        if navio in linha:
            return False
        # else:             BUG
        #     return True   BUG
    return True



def main():
    agua = "#"
    navio = "N"
    acerto = "X"
    erro = "O"
    lista_linhas = [0,1,2,3,4] # tabuleiro 5
    lista_colunas = [0,1,2,3,4,5,6,7,8,9] # por 10

    tabuleiro = criar_tabuleiro(agua)
    tabuleiroIa = criar_tabuleiro(agua)
    tabuleiroIaVerdadeiro = criar_tabuleiro(agua)

    print("Posicione seus 5 navios")
    for i in range(5):
        print(f"Navio {i+1}:")
        posicionar_pecas(tabuleiro, navio, lista_linhas, lista_colunas) # +linha e coluna aqui

    for i in range(5):
        posicionar_pecas_ia(tabuleiroIaVerdadeiro, navio, lista_linhas, lista_colunas) # +linha e coluna aqui tbm
# adicionado parâmetro navio e tabuleiroIaVerdadeiro em mostrar_tabuleiros
    print("Jogo iniciado!")
    while True:
        mostrar_tabuleiros(tabuleiro, tabuleiroIa, tabuleiroIaVerdadeiro, navio)
        ataque_jogador(tabuleiroIaVerdadeiro, tabuleiroIa, lista_linhas, lista_colunas, navio, acerto, erro) # também
        if verificar_vitoria(tabuleiroIaVerdadeiro, navio):
            mostrar_tabuleiros(tabuleiro, tabuleiroIa, tabuleiroIaVerdadeiro, navio)
            print("Parabéns! Você venceu!")
            print("Obrigado por jogar!")
            print("Jogo feito por:")
            print("Davi Berbek")
            print("Otávio Londero")
            break

        ataque_ia(tabuleiro, lista_linhas, lista_colunas, navio, acerto, erro) # também
        if verificar_vitoria(tabuleiro, navio):
            mostrar_tabuleiros(tabuleiro, tabuleiroIa, tabuleiroIaVerdadeiro, navio)
            print("A IA venceu! Tente novamente.")
            print("Obrigado por jogar!")
            print("Jogo feito por:")
            print("Davi Berbek")
            print("Otávio Londero")
            break

main()