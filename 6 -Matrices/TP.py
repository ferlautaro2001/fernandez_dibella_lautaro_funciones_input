# Matrices ejemplo.

matriz_a = [[3, 9], [1, 4], [8, 2]] # A. 
matriz_b = [[7, 2], [4,2]] # B.

matriz_c = [[0, 0], [0, 0], [0, 0]] # Resultado iniciado en 0. 

for i in range(len(matriz_a)): # Itera a través de toda la matriz A.

    for j in range(len(matriz_b[0])):  # Itera a través de las columnas de B.
        for k in range(len(matriz_b)):  # Itera a través de las filas de B y de las columnas de A.
            matriz_c[i][j] += matriz_a[i][k] * matriz_b[k][j] # Suma el producto cruzado de la fila x columna. 

print(matriz_c) # Resultado.

