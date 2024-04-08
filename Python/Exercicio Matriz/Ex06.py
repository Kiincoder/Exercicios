"""
06) Faça um programa em Python que leia duas listas de números compostas por cinco
elementos informados de maneira ordenada (números em ordem crescente). Crie uma
terceira lista também ordenada, sendo a união das duas primeiras listas. Exiba as listas, e a
soma dos seus elementos contidos.
"""

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
lista3 = []
soma = 0

for elemento in lista1:
  if elemento not in lista2:
    lista3.append(elemento)

for elemento in lista2:
  if elemento not in lista1:
    lista3.append(elemento)

for num in lista3:
  soma += num

print(lista3, soma)