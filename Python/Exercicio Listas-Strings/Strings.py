import random
"""
1) Faça um programa em python que leia uma frase e a passe para maiúscula. Você não
deve utilizar as funções prontas do python para converter para maiúscula ou minúscula.
"""
# def maisculo(string):
#     out = ''
#     if len(string) > 1:
#         for index in string:
#             cod = ord(index)
#             if cod >= ord("a") and cod <= ord("z"):
#                 index = chr(cod - 32)
#             out = out + index
#         return out
#     else:
#         if ord(string) >= ord("a") and ord(string) <= ord("z"):
#             string = chr(ord(string) - 32)
#         return string
    
"""
2) Faça um programa em python que leia uma frase e passe para maiúscula a primeira letra
de cada palavra. Você não deve utilizar as funções prontas do python para converter
para maiúscula ou minúscula.
"""

# def maisculo(string):
#     out = ''
#     if len(string) > 1:
#         for index in string:
#             cod = ord(index)
#             if cod >= ord("a") and cod <= ord("z"):
#                 index = chr(cod - 32)
#             out = out + index
#         return out
#     else:
#         if ord(string) >= ord("a") and ord(string) <= ord("z"):
#             string = chr(ord(string) - 32)
#         return string
  
# def minusculo(string):
#     out = ''
#     if len(string) > 1:
#         for index in string:
#             cod = ord(index)
#             if cod >= ord("A") and cod <= ord("Z"):
#                 index = chr(cod+32)
#             out = out + index
#         return out
#     else:
#         if ord(string) >= ord("A") and ord(string) <= ord("Z"):
#             string = chr(ord(string) + 32)
#         return string

# def procurar(letra, string, cont):
#     char = letra  + string[cont+1] + string[cont+2] + string[cont+3]
#     if char == 'dos ' or char == 'das ' or char == 'da ' or char == 'do ':
#         letra = minusculo(letra)
#     else:
#         letra = maisculo(letra)
#     return letra

# nome = 'sexo anal dos santos'
# nome = minusculo(nome)
# captalizeNome = ""
# cont = 0
# pos_maiscula = 0            


# while (cont < len(nome)):
#     letra = nome[cont]
#     if letra == " ":
#         pos_maiscula = cont + 1
#     elif cont == pos_maiscula:
#         if letra == 'd':
#             letra = procurar(letra, nome, cont)
#         else:
#             letra = maisculo(letra)
#     captalizeNome = captalizeNome + letra
#     cont += 1
    
# print(captalizeNome)

"""
3) Escreva um programa que recebe uma string do usuário e imprime a string invertida.
"""

# palavra = "eric"
# invertida = ""

# cont = (len(palavra) - 1)

# while cont >= 0:
#   letra = palavra[cont]
#   invertida = invertida + letra
#   cont -= 1

# print(invertida) 

"""
4) Escreva um programa que recebe uma string do usuário e imprime a string com todas as
letras maiúsculas convertidas para minúsculas e vice-versa
"""

palavra = "abelha faz mel, que nos faz feliz."
# out = ""

# for letra in palavra:
#   if ord(letra) >= ord("A") and ord(letra) <= ord("Z"):
#     letra = minusculo(letra)
#   elif ord(letra) >= ord("a") and ord(letra) <= ord("z"):
#     letra = maisculo(letra)
#   out = out + letra

# print(out)

"""
5) Escreva um programa que recebe uma frase do usuário e conta o número de palavras na
frase
"""
# c = 1
# for letra in palavra:
#     if letra == " ":
#       c +=  1

# print(c)

"""
6) Faça um programa em python que diga se uma senha digitada é fraca, média ou forte.
● Senha fraca: não possui caracteres especiais, nem letras maiúsculas.
● Senha média: possui letras minúsculas, números e caracteres especiais, mas não
possui letras maiúsculas.
● Senha forte: possui letras minúsculas/maiúsculas, números e caracteres especiais.
"""
# senha = 'xiquinho'

# minus = 0
# maisc = 0
# esp = 0
# num = 0

# for letra in senha:    
#     cod = ord(letra)
#     if cod >= ord("a") and cod <= ord("z"):
#         minus += 1
#     if cod >= ord("A") and cod <= ord("Z"):
#         maisc += 1
#     if cod >= ord("0") and cod <= ord("9"):
#         num += 1
#     if cod >= ord("!") and cod <= ord("/"):
#         esp += 1       

# if minus != 0 and maisc == 0 and num == 0 and esp == 0:
#     print("Senha fraca!")
# elif minus != 0 and num != 0 and esp != 0 and maisc == 0:
#     print("Senha media!")
# elif minus != 0 and num != 0 and esp != 0 and maisc != 0:
#     print("Senha forte!")
# else:
#     print("Senha comum!")

"""
7) Escreva um programa em python que leia um texto e diga se é ou não um palíndromo
(ou seja, se o inverso da string é igual a ela). Não será possível utilizar qualquer função
no python que trabalhe com strings.
Exemplos:
Ama
Mirim
A grama é amarga
"""
  
# string = "A grama é amarga"
# string = minusculo(string)
# palindromo = ''

# for letra in string:
#     if letra == " ":
#         letra = ""
#     palindromo = palindromo + letra

# string = palindromo
# palindromo = ''
# c = len(string) - 1

# while c >= 0:
#     letra = string[c]
#     palindromo = palindromo + letra
#     c -= 1

# if string == palindromo:
#     print("Palindromo")
# else:
#     print("Nao eh")

"""
8) Faça um programa em python que:
● Crie uma senha aleatória de 6 caracteres alfanuméricos (A..Z,0..9);
● Descubra a senha criada (força bruta - tentar todas possibilidades). Obs: para
encontrar a senha, você não pode comparar pedaços da senha, precisa comparar
toda senha (ex: if senha_gerada==senha_tentada: ).
"""

# senha = ''
# senha_gerada = ''
# c = 0 

# while len(senha) != 6:
#     controlador = random.randint(0, 1)
#     if controlador == 0:
#         codNum = random.randint(48, 57)
#         num = chr(codNum)
#         senha += num
#     elif controlador == 1:
#         codLetra = random.randint(65, 90)
#         letra = chr(codLetra)
#         senha += letra 

# while c < len(senha):
#     codLetra = random.randint(65, 90)
#     letra = chr(codLetra) 
#     codNum = random.randint(48, 57)
#     num = chr(codNum)

#     if letra == senha[c]:
#         senha_gerada += letra
#         c += 1
#     elif num == senha[c]:
#         senha_gerada += num
#         c += 1

# print(f"A senha descoberta foi: {senha_gerada}")

"""
9) Escreva um programa em python que leia uma string, e substitua cada segmento de dois
ou mais espaços em branco por um só caractere de espaço. Não deve ser utilizada
qualquer função no python que trabalhe com strings.
"""

# frase = "Jorge    está                triste"
# a = ""
# c = 0
# while c < len(frase):
#     letra = frase[c]
    
#     if letra == " ":
#         m = c
#         m += 1
#         space = frase[m]
#         while space == " ":
#             space = frase[m]
#             letra = ""
#             m += 1

#     a += letra
#     c += 1

# print(a)

"""
10) Faça um programa em python que leia três textos. O programa deve imprimir o primeiro
texto substituindo todas as ocorrências do segundo pelo terceiro. Não deve ser utilizada
qualquer função no python que trabalhe com strings.
"""
