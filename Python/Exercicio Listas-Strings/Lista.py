"""
01) Crie uma lista de nomes de cidades. Peça ao usuário para digitar o nome de uma
cidade e verifique se ela está presente na lista. Se estiver, remova a cidade da lista e
imprima a lista resultante. Caso contrário, imprima uma mensagem dizendo que a
cidade não foi encontrada. Faça 2 versões desse exercício, uma usando a função
“remove” e outra sem usar funções prontas do python.
"""

# cidades = ['rio grande', 'porto alegre', 'canoas']

# cidade = str(input("Qual cidade você procura?"))

# if cidade in cidades:
#     cidades.remove(cidade)
# else:
#     cidades.append(cidade)

# print(cidades)

"""
02) Crie 3 listas que contém o nome de um produto, o seu preço e a quantidade
disponível em estoque. Peça ao usuário para comprar um produto digitando o nome
e a quantidade desejada. Verifique se o produto está disponível em estoque e, se
estiver, atualize a quantidade disponível e informe o total a pagar. Repita esse
processo até que o usuário digite "sair
"""

# produtos = ['banana', 'maça']
# qtd = [25, 12]
# preco = [12, 5]
# total = 0

# while True:
#     print('------------- Lojinha -------------')
#     print('Produto | Preco | Estoque')
#     for i in range(0, len(produtos)):
#         print(f'{produtos[i]} | {preco[i]} R$ | {qtd[i]}')
#     print(' [0] Comprar \n [1] Finalizar Compra ')

#     op = input('> ')

#     if op == '0':
#       compra = input('Qual produto você deseja?')
#       qtd_desej = int(input('Quantos você deseja?'))

#       index = produtos.index(compra)
      
#       if qtd_desej > qtd[index]:
#          print('Quantidade indisponivel!')
#       elif qtd[index] > 0:
#          qtd[index] -= qtd_desej
#       else:
#         print('Quantidade indisponivel!')

#       total = total + (qtd_desej * preco[index])

#     else:
#        print(f'O total da sua compra foi de: {total} R$')
#        break

"""
03) Crie um programa que recebe uma string como entrada e retorna uma nova string
em que cada caractere foi substituído pelo seu código ASCII.
Exemplo:
# Informe o texto: Hello
# Saída esperada: "72 101 108 108 111
"""

# a = input('texto> ')
# ascis = []

# for carac in a:
#   asci = str(ord(carac))
#   ascis.append(asci)

# print(' '.join(ascis))

"""
04) Crie um programa que leia uma string e um número inteiro como chave e retorne
uma nova string em que cada caractere foi deslocado para a direita na sequência de
caracteres ASCII pelo valor da chave.
Exemplo:
# Informe a mensagem: hello
# Informe a chave: 3
# Saída esperada: "khoor"
"""

# palavra = input('Digite a palavra: ')
# chave = int(input('Digite a chave: '))
# palavra_nova = []

# for carac in palavra:
#   asci = ord(carac)
#   newcarac = chr(asci+chave)
#   palavra_nova.append(newcarac)

# print(''.join(palavra_nova))

"""
05) Crie um programa que recebe uma string com letras maiusculas, espaços e números
como entrada e retorna uma nova string em que cada caractere foi convertido para o
código Morse. Código Morse:
Exemplo:
# Informe a mensagem: HELLO 123
# Saída esperada: ".... . .-.. .-.. --- .---- ..--- ...--"
"""

# carac = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
#          'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', 
#          '6', '7', '8', '9', '0']

# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', 
#          '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.---', '--..', '.----', '..---', '...--', '....-', '.....', 
#          '-....', '--...', '---..', '----.', '-----']

# string = input('Digite> ')
# new_string = []

# for letra in string:
#   index = carac.index(letra)
#   new_string.append(morse[index])

# print(' '.join(new_string))
