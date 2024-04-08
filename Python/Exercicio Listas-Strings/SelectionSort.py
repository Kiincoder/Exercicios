def selection_sort(array, tamanho):
    for elemento_i in range(tamanho - 1):
        indice_minimo = elemento_i

        for elemento_j in range(elemento_i + 1, tamanho):
            if array[elemento_j] < array[indice_minimo]:
                indice_minimo = elemento_j
                
        if indice_minimo != elemento_i:
          array[elemento_i], array[indice_minimo] = array[indice_minimo], array[elemento_i]

array = [64, 25, 12, 22, 11]
tamanho = 5
print("Array antes da ordenação:", array)

selection_sort(array, tamanho)

print("Array após a ordenação:", array)
