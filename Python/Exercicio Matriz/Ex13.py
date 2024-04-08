"""
13) Faça uma função, em Python, cujo protótipo é QuantosDias(dia, mes, ano),
que retorne a quantidade de dias do ano até a data informada por parâmetro. Para tanto, é
preciso verificar o número de dias em cada mês. O mês de fevereiro pode ter 28 ou 29 dias,
dependendo se o ano for bissexto (verificar).
"""

def QuantosDias(dia, mes, ano):
  dia_atual = 4
  mes_atual = 10
  ano_atual = 2023

  compara_ano = ano_atual - ano
  compara_mes = mes_atual - mes
  compara_dia = dia_atual - dia

  mes_em_dia = compara_mes * 31

  ano_em_dia = compara_ano * 365

  dia_passados = ano_em_dia + mes_em_dia + compara_dia

  return dia_passados

print(QuantosDias(9, 7, 2005))
