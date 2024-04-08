"""
10) Escreva um programa em Python que calcule o comprimento da mais longa sequência de
espaços em branco em uma string lida.
"""
index = 0
cont = 1

string = ""

while index < len(string):
  if string[index] == " " and string[index + 1] == " ":
    cont += 1
    index += 1
  else:
    index += 1

print(cont)