"""
Faça um programa em Python que leia três listas compostas por cinco números fornecidos
pelo usuário. Crie uma matriz que reúna estas três listas (as listas podem ser as linhas ou as
colunas da matriz). Apresente o conteúdo da matriz, assim como o seu maior valor contido.
"""

lista1 = [5,4,5,5,2]
lista2 = [5,5,5,5,4]
lista3 = [1,2,1,1,1]
maior = 0
matriz_formatada = ''


matriz = [lista1, lista2, lista3]

for linha in matriz:
  for num in linha:
    if num > maior:
      maior = num

for row in matriz:
  row = str(row)
  row = row.replace("]", "|")
  row = row.replace("[", "|")
  row = row.replace(",", " ")
  print(row) 

print("O maior elemento é:", maior)



