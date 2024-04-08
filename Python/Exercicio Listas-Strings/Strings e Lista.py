"""
1)Escreva um programa que leia uma lista de palavras do usuário e retorne outra lista contendo apenas as palavras com mais de 5 caracteres.
"""

# lista = ["jorge", "alberto"]
# five_stack = []
# x = 0 

# while x < len(lista):
#   if len(lista[x]) >= 5:
#       five_stack.append(lista[x])
#   x += 1 

# print(five_stack)

"""
2)Escreva um programa que receba uma lista de números e retorne uma nova lista contendo apenas os números pares.
"""

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# retorno = []

# for num in numeros:
#     if num % 2 == 0:
#       retorno.append(num)

# print(retorno)

"""
3)Escreva um programa que receba duas listas do usuário e retorne uma nova lista contendo apenas os elementos comuns entre as duas listas.
"""

# lista1 = ['abobora', 'leite']
# lista2 = ['leite', 'achocolatado']
# comuns = []

# for elemento in lista1:
#   if elemento in lista2:
#     comuns.append(elemento)

# print(comuns)

"""
4)Dada uma lista de números inteiros informada pelo usuário, escreva um programa em Python que conte quantos números únicos (diferentes) 
estão presentes na lista. A digitação dos elementos da lista deve encerrar quando for digitado o número zero.
"""

# lista1 = [1, 1, 2, 3, 5, 8, 13, 21, 34]
# lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# incomuns = []

# for num in lista1:
  # if num not in lista2:
  #   incomuns.append(num)

# print(incomuns)

"""
5)Faça um programa em python em que o usuário digite uma lista de números inteiros (até digitar zero). 
Após, o programa deve mostrar a frequência de cada número na lista, ou seja, quantos números 1 tem, quantos números 2, etc.
"""

# numeros = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 8, 9]
# num = []
# freq = []


# for elemento in numeros:
#   if elemento in num:
#     position = num.index(elemento)
#     freq[position] += 1
#   else:
#     num.append(elemento)
#     freq.append(1)

# print(num)
# print(freq)


# while True:
#   elemento = int(input("Digite um nuemro(CASO QUEIRA SAIR DIGITE 0)> "))
#   if elemento == 0:
#     break
#   else:
#     numeros.append(elemento)

"""
6)Faça um programa que gerencie uma lista de times de futebol. Você precisa criar um programa que armazene uma lista de times de futebol. 
O programa deve permitir ao usuário adicionar novos times à lista, remover times existentes e exibir a lista completa de times. 
Crie um menu em que o usuário fique escolhendo a opção desejada.
"""

# times = []

# while True:
#   numerador = 1
#   print(20*"#")
#   for time in times:
#     print(f"{numerador} - {time}")
#     numerador += 1
#   print(20*"#")
#   print("Opções: \n 1) Adicionar novo time \n 2) Remover time existente \n 3) Sair")

#   option = input("> ")
#   if option == '1':
#     elemento = input("Qual time você deseja adicionar: ")
#     times.append(elemento)
#   elif option == '2':
#     remover = input("Indique o numero do time que deseja remover: ")
#     times.remove(remover)
#   else:
#     break

"""
7)Faça um programa para reserva de ingressos de um cinema. O usuário pode escolher o lugar a ser reservado (fileira e a poltrona desejada - 10x10).
Escreva um programa em Python que, através de um menu, permita ao usuário reservar ingressos, exibir a disponibilidade de lugares e exibir a lista de lugares reservados. 
"""

# lugares = [['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10'], 
#            ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10'], 
#            ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10'], 
#            ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10'], 
#            ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10'], 
#            ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10'], 
#            ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10'], 
#            ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10'], 
#            ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10'], 
#            ['J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10']]
# reservados = []
# disponiveis = lugares

# while True:
#   print(80*"#")
#   print("Escolha a opcao: \n 1) Comprar ingresso \n 2) Sair")
#   option = input("> ")

#   if option == '1':
#     print("############################### DISPONIVEIS ##################################### \n")
#     for i in disponiveis:
#         print(i)
#     print("\n",80*"#")
#     comprar = input("Escolha o lugar> ").upper()
#     reservados.append(comprar)
#     for elemento in disponiveis:
#       for a in elemento:
#         if a in reservados:
#           local = elemento.index(a)
#           elemento[local] = "❌"
#   else:
#     break

"""
8) O algoritmo bag-of-words é uma representação simplificada usada no
processamento de linguagem natural. Nesse modelo, um texto é representado como
a bolsa de suas palavras, desconsiderando a gramática e até mesmo a ordem das
palavras, mas mantendo a multiplicidade, ou seja, a quantidade de vezes que cada
palavra aparece. Faça um programa em python que implemente o “bag-of-words”,
contando quantas vezes cada palavra aparece em um texto e após construa um
gráfico com o resultado.
"""
# texto = "O jose, muito funny é muito divertido, legal. Amo ele."
# texto = texto.replace(", ", " ").replace(".", "").lower()
# txt = texto.split(" ")
# palavras = []
# freq = []

# for elemento in txt:
#   if elemento in palavras:
#     position = palavras.index(elemento)
#     freq[position] += 1
#   else:
#     palavras.append(elemento)
#     freq.append(1)

# c = 0
# while c < len(freq):
#   print(f'{palavras[c]}, {freq[c]}')
#   c += 1

"""
9) Implemente um programa em python que recebe um texto como entrada e realiza a
seguinte análise:
a) Conte e mostre o número total de caracteres no texto (incluindo espaços em
branco).
b) Conte e mostre o número total de palavras no texto.
c) Conte e mostre o número total de frases no texto.
Obs: considere que uma palavra é uma sequência de caracteres separada
por espaços em branco e uma frase é uma sequência de palavras terminada
por um ponto, ponto de exclamação ou ponto de interrogação
"""

# texto = "A expressão Lorem ipsum em design gráfico e editoração é um texto padrão em latim utilizado na produção gráfica. Alou roberta. Jorge é legal"
# caracteres = len(texto)

# frases = texto.split(".")
# if '' in frases:
#   del(frases[-1])
# num_frases = len(frases)

# txt = texto.replace(", ", " ").replace(".", "").lower()
# txt = txt.split(" ")
# palavras = len(txt)

# print(f' Numero de frases: {num_frases}\n Numero de palavras: {palavras}\n Numero de caracteres: {caracteres}')

"""
10) Faça um programa em python que receba uma lista de números inteiros como
entrada e retorne a maior soma dos números ímpares consecutivos da lista. Caso
não haja números ímpares na lista, o programa deve retornar 0.
Exemplo de uso da função:

lista = [1, 2, 3, 5, 6, 7, 9, 10]
Saída esperada:16
"""

# lista = [1, 2, 3, 5, 5, 6, 7, 9, 10]

# maior_soma = 0
# soma_atual = 0

# for num in lista:
#     if num % 2 != 0:  
#         soma_atual += num
#         if soma_atual > maior_soma:
#             maior_soma = soma_atual
#     else:
#         soma_atual = 0
  
# print(maior_soma)