import random

"""
17) Escreva um programa que leia diversos números até que o usuário digite zero. Em
seguida escreva a média dos números digitados.
"""

# sum = 0
# count = 0

# while True:
#     n = int(input("Digite um numero: "))
#     if n != 0:
#         sum += n
#         count += 1
#     else:
#         med = sum/count
#         print(med)
#         break

"""
18) .Escreva um programa que leia diversos funcionários e seu respectivo salario, ate que
o nome de um funcionário seja “fim”. Em seguida escreva:
a) O nome do funcionário com maior salário
b) O nome do funcionário com menor salário
c) A média dos salários digitados
"""
# c = 0
# sum = 0 
# maior = 0
# menor = 999999999
# maiorNome = ''
# menorNome = ''

# while True:
#     nome = input("Nome: ")
    
#     if nome == 'fim':
#         print(20*"#")
#         print(f' Maior: {maiorNome}|{maior} \n Menor: {menorNome}|{menor} \n Media salarial: {med}')
#         break
#     else:
#         salario = float(input(f"Salario de {nome}: "))

#         sum += salario
#         c += 1
        
#         if salario > maior:
#             maior = salario
#             maiorNome = nome
#         else:
#             if salario < menor:
#                 menor = salario
#                 menorNome = nome
        
                
"""
19) Escreva um programa de adivinhação de número. O programa deve conter um
número secreto entre 1 e 1.000.000. O usuário deve chutar um número e o
programa deve dizer se o número chutado é maior ou menor que o número secreto.
O usuário deve tentar até acertar o número secreto. O código abaixo mostrar como
sortear um número aleatório entre 0 e 10 em python:
"""
# n = 0

# secreto =  random.randint(1, 1000)
# print(secreto)

# while n != secreto:
#     n = int(input("Digite um numero: "))

#     if n > secreto:
#         print("O numero secreto é menor!")
#     else:
#         print("O numero secreto é maior!")

# print("VOCE ACERTOU!!!!!")

"""
20) Faça um programa em python que leia um valor inteiro X. Em seguida apresente os 6
valores ímpares consecutivos a partir de X, inclusive o X se for o caso. Por exemplo,
para o número 8, a saída será “9,11,13,15,17,19”.
"""
# c = 0
# n = int(input("Digite um numero: "))

# while c < 6:
#     n += 1
#     if n % 2 != 0:
#         print(n)
#         c += 1

"""
21) Escreva um programa que leia dois valores x e y. Em seguida escreva quais são os
números primos contidos neste intervalo. Por exemplo, para x=3 e y=14 escreva:
3,5,7,11,13. Verifique se o usuário digitou x e y de modo que x<y.
"""
    
# x = int(input("Digite um numero> "))
# y = int(input("Digite um numero> "))
# d = 0
# c = 1

# while x < y:
#     while c <= x:
#         if x % c == 0:
#             d += 1
#             c += 1
#         else:
#             c += 1
#     if d == 2:
#         print(x)
#         x +=  1
#         c = 1
#         d = 0
#     else:
#         x += 1
#         c = 1
#         d = 0

"""
22) Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor
e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Faça
um programa em Python que receba o nome do(a) ginasta, e as notas de sua
apresentação dadas pelos sete jurados. Ao final, informe a melhor nota, a pior nota e
a sua média final, conforme a descrição acima informada (ou seja, retirar a melhor e
a pior nota para calcular a média). As notas não são informadas em ordem (crescente
ou decrescente).
"""

# c = 1
# sum = 0

# nome = input('Digite o nome> ')

# while c <= 7:
#     nota = int(input('Digite a nota> '))

#     if c == 1:
#         maior = nota
#         menor = nota
#     else:
#         if nota > maior:
#             maior = nota
#         if nota < menor:
#             menor = nota

#     sum += nota
#     c += 1

# media = (sum - (menor + maior))/5
    
# print(20*"#")
# print(f' Sua melhor nota foi: {maior} \n Sua pior nota foi: {menor} \n Sua media foi de: {media} ')

"""
23) Considere uma sequência de números que atende a todos critérios abaixo: a - Possui
sempre 2 dígitos , nem mais , nem menos . b - A representação do número possui
pelo menos um dígito 1 ou um dígito 2. c - O número é múltiplo de 3. Faça um
programa que implemente e mostre essa sequência. obs: tem que usar repetição
para mostrar a sequência. Não pode mostrar os números “na mão”.
"""
# x = 10        

# while x >= 10 and x < 100:
#     if x % 3 == 0:
#         if x % 10 == 1 or x % 10 == 2 or x // 10 == 1 or x // 10 == 2:
#             print(x)
#             x += 1
#         else:
#             x += 1
#     else:
#         x += 1

"""
24) Construa um programa em Python que escreva uma contagem de 10 (dez) minutos,
ou seja, mostre 0:00, e então 0:01, 0:02, ..., 0:58, 0:59, 1:00, 1:01, ..., até 10:00.
"""

# objetivo = 10
# minuto = 0
# segundos = 0

# while minuto < objetivo:
#     if segundos >= 60:
#         minuto = segundos // 60
#         segundo = segundos % 60
#         segundos += 1
#         if segundo < 10:
#             print(f'{minuto}:0{segundo}')
#         else:
#             print(f'{minuto}:{segundo}')
#     else:
#         if segundos < 10:
#             print(f'0:0{segundos}')
#         else:
#             print(f'0:{segundos}')
#         segundos += 1

"""
25) Faça um programa em python que desenhe uma pirâmide conforme 2 dados
informados pelo usuário. O primeiro dado indica o "tijolo" e o segundo a quantidade
de andares.
Ex: Informe o tijolo: A
Informe a quantidade de andares: 5
    A
   AAA
  AAAAA
 AAAAAAA
AAAAAAAAA
"""
# FORMA 1 DE REALIZAR O EXERCICIO

# n = int(input("Digite a quantidade de andares: "))
# tijolo = str(input("Digite o tijolo: "))
# c2 = 1
# c = 0
# k = n - 1
# i = 0

# while c < n:
#     j = k
#     while j > 0:
#         print(end=" ")
#         j -= 1        
#     while i < c2:
#         i += 1
#         print(i*f'{tijolo} ', end="")
#     print("\r")
#     k = k - 1
#     c += 1
#     c2 = c2 + 1


# FORMA 2 DE REALIZAR O EXERCICIO

# n = int(input("Digite a quantidade de andares: "))
# tijolo = input("Digite o tijolo: ")
# c = 0
# k = n - 1
# i = 0
# m = 0

# while c < n:
#     j = k
#     i = 0
#     while j > 0:
#         print(end=" ")    
#         j -= 1        
#     while i <= m:
#         print(tijolo, end=" ")
#         i += 1
#     m += 1
#     print("\r")
#     k = k - 1
#     c += 1


