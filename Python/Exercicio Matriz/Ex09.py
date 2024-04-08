"""
9) Faça um programa em Python para jogar o “jogo da velha”. O algoritmo deve permitir que
dois jogadores joguem uma partida, usando o computador para ver o tabuleiro. Cada
jogador vai alternadamente informando a posição onde deseja colocar a sua peça (O ou
X). O programa deverá impedir jogadas inválidas, e determinar automaticamente quando o
jogo terminou, e quem foi o vencedor (jogador1 ou jogador2). A cada nova jogada, o
programa deve atualizar a situação do tabuleiro na tela.
"""


def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
  for linha in tabuleiro:
    cont = 0
    for i in linha:
       if i == jogador:
        cont += 1
        if cont == 3:
          return True

  for coluna in range(3):
    cont = 0
    for linha in range(3):
      elemento = tabuleiro[linha][coluna]
      if elemento == jogador:
        cont += 1
        if cont == 3:
          return True

  if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
      return True

  if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
      return True





jogadas = 0
tabuleiro = [["X", " ", " "], ["X", " ", " "], ["X", " ", " "]]
jogador1 = "X"
jogador2 = "O"
jogador_atual = jogador1

while jogadas < 9:
  mostrar_tabuleiro(tabuleiro)
  print(f"É a vez do jogador {jogador_atual}")

  linha = int(input("Digite a linha (0, 1 ou 2): "))
  coluna = int(input("Digite a coluna (0, 1 ou 2): "))

  if linha < 0 or linha > 2 or coluna < 0 or coluna > 2 or tabuleiro[linha][coluna] != " ":
      print("Jogada inválida!")

  tabuleiro[linha][coluna] = jogador_atual

  verificar_vitoria(tabuleiro, jogador_atual)

  if verificar_vitoria(tabuleiro, jogador_atual):
      mostrar_tabuleiro(tabuleiro)
      print(f"O jogador {jogador_atual} venceu!")
      break
   
  if jogador_atual == jogador1:
    jogador_atual = jogador2

  elif jogador_atual == jogador2:
    jogador_atual = jogador1

  jogadas += 1

if verificar_vitoria(tabuleiro, jogador_atual) == False:
  mostrar_tabuleiro(tabuleiro)
  print("Deu velha!")


