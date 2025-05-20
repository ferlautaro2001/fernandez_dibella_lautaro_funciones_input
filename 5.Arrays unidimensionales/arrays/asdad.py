matriz = [[1, 2], [3, 4]]

for fila_indice in range(len(matriz)): # Itera sobre los índices de las filas
    for columna_indice in range(len(matriz[fila_indice])): # Itera sobre los índices de las columnas DE ESA FILA
        print(f"Elemento en ({fila_indice}, {columna_indice}): {matriz[fila_indice][columna_indice]}")

# O de forma más directa si no necesitas los índices:
for fila_actual in matriz: # fila_actual es una de las listas internas
    for elemento in fila_actual: # elemento es un valor dentro de la lista interna
        print(elemento, end=" ") # 'end=" "' imprime en la misma línea separado por espacio
    print() # Nueva línea después de cada fila