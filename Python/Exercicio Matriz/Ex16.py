"""
16) Uma universidade deseja fazer um levantamento a respeito de seu processo de seleção.
Para cada curso, é fornecido um arquivo texto com o seguinte conjunto de valores:
Nome do curso;
Código do curso;
Número de vagas;
Número de candidatos do sexo masculino;
Número de candidatos do sexo feminino
Fazer um programa em Python que:
• Calcule e escreva, para cada curso, o número de candidatos por vaga e a porcentagem de
candidatos do sexo feminino (escreva também o código correspondente do curso);
• Determine o maior número de candidatos por vaga e escreva esse número juntamente
com o código do curso correspondente (supor que não haja empate);
• Calcule e escreva o total de candidatos.
"""


def relacaoVagaCand(arquivo, index):
    nome_curso = arquivo[index][0]
    vagas_f = int(arquivo[index][-1])

    vagas = int(arquivo[index][2]) 
    qtd_candidatos = int(arquivo[index][3]) + int(arquivo[index][4])

    rel_vaga_cand = qtd_candidatos/vagas

    porcem_fem = (vagas_f * 100)/vagas


    return [nome_curso, rel_vaga_cand, porcem_fem]



def totalCandidatos(arquivo, index):
  cand_f = int(arquivo[index][-1])
  cand_m = int(arquivo[index][-2])

  return cand_f + cand_m


def maiorRelacaoVaga(arquivo, index):
  maior = 0
  lista = relacaoVagaCand(arquivo= arquivo, index= index)
  

  for i in range(len(tabela_cursos)):
    if lista[i] > maior:
      maior = lista[1]
      num_curso = arquivo[i][1]

  return [num_curso, maior]

arquivo = open("Lista Matriz\curso.txt", "r")
tabela_cursos = []

for linha in arquivo:
  linha = linha.replace("\n", "")
  linha = linha.split(";")
  tabela_cursos.append(linha)

for i in range(len(tabela_cursos)):
  lista = relacaoVagaCand(tabela_cursos, i)

print(lista, maiorRelacaoVaga(arquivo))
  