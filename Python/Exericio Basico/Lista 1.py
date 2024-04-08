"""
1) Faça um programa que, ao receber os valores da largura e do comprimento de uma
figura geométrica, mostre se esta é um quadrado ou apenas um retângulo. Caso um
valor seja menor ou igual a zero, deve-se mostrar um erro. 
"""

# largura = float(input('Informe a largura:')) 
# altura = float(input('Informe a altura:'))

# if largura or altura > 0:
#     if largura == altura:
#         print('Quadrado')
#     else:
#         print('Retângulo') 

# else:
#     print('Valores invalidos!')

"""
2) Faça um programa em python que pergunte ao usuário o seguinte:
    a) A viagem custará menos de R$ 30?
    b) Terá Wifi?
    c) Terá piscina?
    d) Terá churrasqueira?
O programa deverá mostrar se a viagem ocorrerá de acordo com as seguintes regras:
- Deverá custar menos de R$ 30
- Tem que ter wifi e piscina
- Se não tiver wifi ou piscina, tem que ter churrasqueira
"""

# preço = int(input('Preço do aluguel: '))
# piscina = input('Tem piscina? ')
# wifi = input('Tem wifi? ')
# churras = input('Tem churrasco? ')
# ruim = 'Pessimo lugar'
# bom = 'Otimo lugar'

# if preço > 30:
#     print(ruim)
# else:
#     if piscina == 's' and wifi == 's':
#         print(bom)
#     else:
#         if churras == 's':
#             print(bom)
#         else:
#             print(ruim)

"""
3) Construa um programa em python que, informadas três medidas a, b e c pelo
usuário, verifique se elas podem ser lados de um triângulo. Se não puderem ser,
primeiramente o algoritmo deve informar isso. Se for possível serem lados de
triângulo, deve dizer qual tipo de triângulo pode ser construído com essas medidas
(isósceles, escaleno ou equilátero). A condição para formar um triângulo:
comprimento do maior segmento seja inferior à soma dos comprimentos dos dois
menores.
"""

# a = float(input('Informe o valor do lado A:'))
# b = float(input('Informe o valor do lado B:'))
# c = float(input('Informe o valor do lado C:'))

# if (a+b) > c and (a+c) > b and (c+b) > a:

#     if a == b and a == c:
#         print('Equilatero')

#     elif a != b != c != a:
#         print('Escaleno')

#     else:
#         print('Isosceles')

# else:
#     print('Triangulo inválido!')

"""
4) Crie um programa em Python que leia as notas do estudante nos 4 bimestres da
nossa disciplina e a frequência (em porcentagem). A seguir informe se o estudante
passou por média, rodou ou ficou em exame. Para passar por média, o estudante
deve ter média maior ou igual a 7. Estudante com média abaixo de 3 roda sem ao
menos fazer o exame. O estudante que tiver menos de 75% de frequência também
está rodado na disciplina.
"""

# nota1 = float(input('Insira a sua nota 1:'))
# nota2 = float(input('Insira a sua nota 2:'))
# nota3 = float(input('Insira a sua nota 3:'))
# nota4 = float(input('Insira a sua nota 4:'))

# freq = float(input('Insira sua frequência:'))

# media = (nota1 + nota2 + nota3 + nota4) / 4

# if freq >= 75:
#     if media >= 7:
#         print('Passou')
#     elif media <= 3:
#         print('Rodou')
#     else:
#         print('Exame')
# else:
#     print('Rodou')

"""
5) Faça um programa em python que leia 3 números e os mostre em ordem crescente.
"""
# n1 = int(input("Digite um número:"))
# n2 = int(input("Digite um número:"))
# n3 = int(input("Digite um número:"))

# if n1 >= n2 and n1 >= n3:
# 	if n2 > n3:
# 		print(n3, n2, n1)
# 	else:
# 		print(n2, n3, n1)
	
# elif n2 >= n1 and n2 >= n3:
# 	if n1 > n3:
# 		print(n3, n1, n2)
# 	else:
# 		print(n1, n3, n2)
		
# else:
# 	if n1 >= n2:
# 		print(n2, n1, n3)

# 	else:
# 		print(n1, n2, n3)

"""
6) Faça um programa em python que leia o nome de 4 times de futebol que estão em
uma semifinal. Após, leia os gols das duas partidas: time 1 x time 2 e time 3 x time 4.
Os times vencedores devem ir para a final. Caso haja empate, deve-se perguntar ao
usuário qual time se classificou. Por fim, deve-se ler os gols da final e mostrar qual
time foi campeão (se empatar, perguntar quem foi campeão).
"""
# gols_time1 = int(input('Quantos gols o time 1 fez:'))
# gols_time2 = int(input('Quantos gols o time 2 fez:'))
# gols_time3 = int(input('Quantos gols o time 3 fez:'))
# gols_time4 = int(input('Quantos gols o time 4 fez:'))

# ganhador_semiA = ''
# ganhador_semiB = ''

# if gols_time1 > gols_time2:
#     ganhador_semiA = 'Time 1'

# elif gols_time1 == gols_time2:
#     ganhador_semiA = str(input('Qual time venceu na moeda?'))

# else:
#     ganhador_semiA = 'Time 2'


# if gols_time3 > gols_time4:
#     ganhador_semiB = 'Time 3'

# elif gols_time3 == gols_time4:
#     ganhador_semiB = str(input('Qual time venceu na moeda?'))

# else:
#     ganhador_semiB = 'Time 4'


# gols_final1 = int(input(f'Quantos gols o time {ganhador_semiA} fez na final:'))
# gols_final2 = int(input(f'Quantos gols o time {ganhador_semiB} fez na final:'))

# if gols_final1 > gols_final2:
#     print(f'O ganhador foi o time {ganhador_semiA}')
# elif gols_final1 == gols_final2:
#     g = input("Diga quem ganhou:")
#     print(f'O ganhador foi o time {g}')
# else:
#     print(f'O ganhador foi o time {ganhador_semiB}')

"""
7) Crie um programa em Python que leia o rendimento mensal do usuário, qual o modelo de
imposto (sem correção/com correção das perdas no governo Bolsonaro) e retorne o quanto
ele deve pagar de imposto.
"""

# modelo = int(input('Escolha a opção de modelo: \n(1) Modelo sem correção \n (2) Modelo Bolsonaro \n (3) Modelo com  correção integral'))
# renda = int(input('Informe sua renda:'))

# if modelo == 1:
#     if renda > 1903.98 and renda <= 2826.65:
#         pagar = (renda * 0.075) - 142.80
#     elif renda > 2826.65 and renda <= 3751.05:
#         pagar = (renda * 0.15) - 354.80
#     elif renda > 3751.05 and renda <= 4664.68:
#         pagar = (renda * 0.225) - 636.13
#     else:
#         pagar = (renda * 0.275) - 869.36


# elif modelo == 2:
#     if renda > 2500.44 and renda <= 3712.16:
#         pagar = (renda * 0.075) - 187.54
#     elif renda > 3712.16 and renda <=  4926.14:
#         pagar = (renda * 0.15) - 465.95
#     elif renda > 4926.14 and renda <= 6125.99:
#         pagar = (renda * 0.225) - 835.41
#     else:
#         pagar = (renda * 0.275) - 1141.71


# elif modelo == 3:
#     if renda > 4710.49 and renda <= 6993.20:
#         pagar = (renda * 0.075) - 353.29
#     elif renda > 6993.2 and renda <= 9280.19:
#         pagar = (renda * 0.15) - 877.78 
#     elif renda > 9280.19 and renda <= 11540.53 :
#         pagar = (renda * 0.225) - 1573.80
#     else:
#         pagar = (renda * 0.275) - 2150.82

# else:
#     print('Informe uma opção válida')

# print(f'{pagar:,.2f}')
