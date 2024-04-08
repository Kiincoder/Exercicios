"""
11) Implementar um programa para somar matrizes.
Obs.: as matrizes obrigatoriamente têm a mesma dimensão. Ex.:
"""

matriz_A = [[1, 2, 3],[3, 2, 1],[0, 1, 2]]
matriz_B = [[1, 2, 3],[3, 2, 1],[0, 1, 2]]
matriz_C = [[], [], []]

for i in range(len(matriz_A)):
  for j in range(len(matriz_A[i])):
    resultado = matriz_A[i][j] + matriz_B[i][j] 
    matriz_C[i].append(resultado)

print(matriz_C)