def es_digito(caracter):
    """Retorna True si el carácter es un dígito ('0' - '9'), False si no."""
    return '0' <= caracter <= '9'


def es_cadena_digitos_positivos(cadena):
    """Retorna True si todos los caracteres de la cadena son dígitos, False si no o cadena vacía."""
    if not cadena:
        return False
    for caracter in cadena:
        if not es_digito(caracter):
            return False
    return True


def obtener_tamano_matriz():
    """Solicita al usuario un entero positivo para el tamaño de la matriz."""
    while True:
        entrada = input("Ingrese el tamaño de la matriz (n, ej: 3): ")
        if es_cadena_digitos_positivos(entrada):
            tamaño = int(entrada)
            if tamaño > 0:
                return tamaño
        print("Error: n debe ser un número entero positivo.")


def ingresar_matriz_manualmente(tamaño):
    """Solicita al usuario que ingrese números positivos para una matriz cuadrada de tamaño dado."""
    matriz = [[0] * tamaño for _ in range(tamaño)]

    print(f"Ingrese los números para la matriz de {tamaño}x{tamaño}:")
    for fila in range(tamaño):
        for columna in range(tamaño):
            while True:
                valor = input(f"  Elemento ({fila + 1},{columna + 1}): ")
                if es_cadena_digitos_positivos(valor):
                    matriz[fila][columna] = int(valor)
                    break
                else:
                    print("Error: Ingrese un número entero positivo válido.")
    return matriz


def mostrar_matriz_simple(matriz):
    """Muestra la matriz de forma simple."""
    if not matriz:
        return
    print("\nMatriz ingresada:")
    for indice_fila in range(len(matriz)):
        linea_matriz = ""
        for indice_columna in range(len(matriz[indice_fila])):
            if indice_columna > 0:
                linea_matriz += " "
            linea_matriz += str(matriz[indice_fila][indice_columna])
        print(linea_matriz)
    print()


def calcular_constante_magica(tamaño):
    """Calcula la constante mágica para un cuadrado de tamaño n."""
    return (tamaño * (tamaño * tamaño + 1)) // 2


def verificar_definicion_numeros(matriz, tamaño):
    """
    Verifica que la matriz tenga dimensiones correctas y contenga
    números únicos del 1 al n*n.
    """
    if not matriz or len(matriz) != tamaño:
        return False

    max_valor = tamaño * tamaño
    contador = [0] * (max_valor + 1)  # índice 0 no se usa

    for fila in matriz:
        if not fila or len(fila) != tamaño:
            return False
        for numero in fila:
            if numero < 1 or numero > max_valor:
                return False
            contador[numero] += 1

    for i in range(1, max_valor + 1):
        if contador[i] != 1:
            return False

    return True


def es_cuadrado_magico(matriz, tamaño):
    """Determina si la matriz es un cuadrado mágico."""
    # Si la disposición de la matriz es correcta. 
    if not verificar_definicion_numeros(matriz, tamaño):
        return False

    constante = calcular_constante_magica(tamaño)

    # Verificar filas
    for fila in matriz:
        if sum(fila) != constante:
            return False

    # Verificar columnas
    for col in range(tamaño):
        suma_columna = sum(matriz[fila][col] for fila in range(tamaño))
        if suma_columna != constante:
            return False

    # Verificar diagonal principal
    if sum(matriz[i][i] for i in range(tamaño)) != constante:
        return False

    # Verificar diagonal secundaria
    if sum(matriz[i][tamaño - 1 - i] for i in range(tamaño)) != constante:
        return False

    return True


def main():
    print("--- Verificador de Cuadrado Mágico (Ultra Simplificado) ---")
    tamaño = obtener_tamano_matriz()
    matriz = ingresar_matriz_manualmente(tamaño)
    mostrar_matriz_simple(matriz)

    if es_cuadrado_magico(matriz, tamaño):
        print("Resultado: La matriz ES un cuadrado mágico.")
    else:
        print("Resultado: La matriz NO es un cuadrado mágico.")


main()
