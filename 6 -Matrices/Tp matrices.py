matriz_a = [[1, 2, 3], [4, 5, 6]]  # Matriz A (2x3)
matriz_b = [[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]]  # Matriz B (3x4)
matriz_c = [[0, 0, 0, 0], [0, 0, 0, 0]]  # Matriz resultado (2x4)

for i in range(len(matriz_a)):  # Iteramos filas de A
    for j in range(len(matriz_b[0])):  # Iteramos columnas de B
        for k in range(len(matriz_b)):  # Iteramos filas de B / columnas de A
            matriz_c[i][j] += matriz_a[i][k] * matriz_b[k][j]

# Mostramos resultado fila por fila
print("Resultado de la multiplicación (matriz_c):")
for fila in matriz_c:
    print(fila)  # Imprimimos cada fila en una línea nueva