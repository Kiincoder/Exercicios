"""
12) Implementar um programa para multiplicar matrizes.
Obs (nro de elementos em cada dimensão):
1ª matriz = (Linhas1 x Colunas1)
2ª matriz = (Linhas2 x Colunas2)
"""

matriz_A = [[1, 2, 3],[3, 2, 1],[0, 1, 2]]
matriz_B = [[1, 2, 3],[3, 2, 1],[0, 1, 2]]
matric_C = [[], [], []]

for i in range(len(matriz_A)):
  for j in range(len(matriz_B[0])):
    som = 0
    for k in range(len(matriz_B)):
      resultado = matriz_A[i][k] * matriz_B[k][j]
      som += resultado
    matric_C[i].append(som)

print(matric_C)