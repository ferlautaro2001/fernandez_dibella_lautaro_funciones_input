def mostrar_matriz_simple(matriz):
    """Muestra la matriz de forma simple."""
    print("\nMatriz ingresada:")
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()
    print()

def calcular_constante_magica(dimension):
    """Calcula la constante mágica para un cuadrado de tamaño n."""
    return (dimension * (dimension * dimension + 1)) // 2

def verificar_numeros_validos(matriz, dimension):
    """
    Verifica que la matriz tenga dimensiones correctas y contenga
    números únicos del 1 al n*n.
    """
    maximo_valor = dimension * dimension
    contador_ocurrencias = [0] * (maximo_valor + 1)

    for fila in matriz:
        for numero in fila:
            if numero < 1 or numero > maximo_valor:
                return False
            contador_ocurrencias[numero] += 1

    for numero in range(1, maximo_valor + 1):
        if contador_ocurrencias[numero] != 1:
            return False

    return True

def es_cuadrado_magico(matriz, dimension):
    """Determina si la matriz es un cuadrado mágico."""
    if not verificar_numeros_validos(matriz, dimension):
        return False

    constante_magica = calcular_constante_magica(dimension)

    # Verificar filas
    for fila in matriz:
        if sum(fila) != constante_magica:
            return False

    # Verificar columnas
    for columna in range(dimension):
        suma_columna = 0
        for fila in range(dimension):
            suma_columna += matriz[fila][columna]
        if suma_columna != constante_magica:
            return False

    # Verificar diagonal principal
    suma_diagonal_principal = 0
    for i in range(dimension):
        suma_diagonal_principal += matriz[i][i]
    if suma_diagonal_principal != constante_magica:
        return False

    # Verificar diagonal secundaria
    suma_diagonal_secundaria = 0
    for i in range(dimension):
        suma_diagonal_secundaria += matriz[i][dimension - 1 - i]
    if suma_diagonal_secundaria != constante_magica:
        return False

    return True

def main():
    print("--- Verificador de Cuadrado Mágico (Hardcoded) ---")

    # Ejemplo: Cuadrado mágico de 3x3
    matriz_cuadrada = [
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 8]
    ]
    dimension = len(matriz_cuadrada)

    mostrar_matriz_simple(matriz_cuadrada)

    if es_cuadrado_magico(matriz_cuadrada, dimension):
        print("Resultado: La matriz ES un cuadrado mágico.")
    else:
        print("Resultado: La matriz NO es un cuadrado mágico.")

main()
