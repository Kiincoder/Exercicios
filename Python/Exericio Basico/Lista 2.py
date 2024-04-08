"""
08) Escreva um programa que mostre os números de 1 a 10.
"""
# numero = 0

# while numero < 10:
#     numero = numero + 1
#     print(numero)   

"""
09) Escreva um programa que mostre os números de 10 a 1.
"""

# numero = 11

# while numero > 0:
#     numero = numero - 1
#     print(numero)

"""
10) Escreva um programa que mostre os números pares de 1 a 200.
"""

# numero = 0

# while numero < 200:
#     numero = numero + 1
#     if numero % 2 == 0:
#         print(numero)

"""
11) Escreva um programa que mostre a tabuada (0 a 10) de um número fornecido pelo usuario.
"""

# numero = int(input("Digite o numero da tabuada desejada:"))

# c = 0

# while c < 10:
#     r = numero * c 
#     print(f"{numero} X {c} = {r}")
#     c = c + 1

"""
12) Escreva um programa que mostre a seguinte sequência de números para um valor N informado pelo usuario:
"""

# n = int(input("Digite um numero: "))
# i = 0

# while i < n:
#     i += 1
#     a = str(i)
#     print(i*a)

# FORMA CORRETA/OUTRA FORMA

# n = int(5)
# j = 1
# a = 0
# m = 0

# while j <= n:
#   i = 0 
#   a += 1
#   while i <= m:
#     print(a, end=" ")
#     i += 1
#   m += 1
#   print()
#   j += 1

"""
13) Escreva um programa que calcule e mostre a soma dos números de 1 a N. Não utilize as equações de progressão aritmética.
"""

# n = int(input("Digite"))
# c = 0
# sm = 0 

# while c <= n:
#     r = sm + c
#     sm = sm + c
#     c = c + 1

# print(r)  

"""
14) Escreva um programa que receba um número inteiro positivo do usuário e verifique se ele é primo.
"""

# n = int(input("digita "))
# c = 1
# d = 0

# while c < n:
#     if n % c == 0:
#         d += 1
#         c += 1
#     else:
#         c += 1
    
# if d > 2:
#     print("composto")
# else:
#     print("primo")

""" 
15) Escreva um programa que mostre a sequência de Fibonacci até o enésimo termo (n
deve ser informado pelo usuário). A sequência de Fibonacci é aquela em que cada
termo é a soma dos dois termos anteriores. Por exemplo, para n=8 escreva 0, 1, 1, 2,
3, 5, 8 e 13.
"""
# n = int(input("Digite: "))
# i = 1
# n1 = 0
# n2 = 1

# if n = 1 or n == 2:
#     print("1")
# else:
#     while i < n:
#         s = n1 + n2
#         n1 = n2
#         n2 = s
#         i += 1
#     print(s)

"""
16) Escreva um programa que calcule o fatorial de um número fornecido pelo usuário. O
fatorial de um número n é o produto de todos os números inteiros de 1 a n.
"""

# n = int(input("Digite: "))
# arm = n

# while n != 1:
#     arm = arm * (n - 1) 
#     n = n - 1

# print(arm)

