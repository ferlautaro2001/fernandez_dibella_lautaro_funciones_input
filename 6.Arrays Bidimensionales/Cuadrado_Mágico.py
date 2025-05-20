def _es_caracter_digito(caracter):
    """Retorna True si el carácter es un dígito ('0' - '9'), False si no."""
    return '0' <= caracter <= '9'

def _es_cadena_digitos_positivos(cadena):
    """Verifica si todos los caracteres en la cadena son dígitos ('0'-'9')."""
    es_valida = True
    if not cadena:
        es_valida = False
    else:
        for indice_caracter in range(len(cadena)):
            if not _es_caracter_digito(cadena[indice_caracter]):
                es_valida = False
                break
    return es_valida


# --- Funciones del programa ---
def obtener_tamano_matriz():
    """Solicita y valida que el tamaño n sea un entero positivo."""
    while True:
        entrada_tamano_str = input("Ingrese el tamaño de la matriz (n, ej: 3): ")
        if _es_cadena_digitos_positivos(entrada_tamano_str):
            tamano = int(entrada_tamano_str)
            if tamano > 0:
                return tamano
        print("Error: n debe ser un número entero positivo.")


def ingresar_matriz_manualmente(tamano_matriz):
    """Permite ingresar la matriz manualmente. Solo valida que se ingresen números positivos."""
    matriz = [None] * tamano_matriz
    for indice_fila in range(tamano_matriz):
        matriz[indice_fila] = [0] * tamano_matriz

    print(f"Ingrese los números para la matriz de {tamano_matriz}x{tamano_matriz}:")
    for indice_fila in range(tamano_matriz):
        for indice_columna in range(tamano_matriz):
            while True:
                valor_ingresado = input(f"  Elemento ({indice_fila + 1},{indice_columna + 1}): ")
                if _es_cadena_digitos_positivos(valor_ingresado):
                    matriz[indice_fila][indice_columna] = int(valor_ingresado)
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


def calcular_constante_magica(tamano_matriz):
    """Calcula la constante mágica M."""
    return (tamano_matriz * ((tamano_matriz * tamano_matriz) + 1)) // 2


def verificar_definicion_numeros(matriz, tamano_matriz):
    """
    Verifica que la matriz contenga números enteros del 1 al n*n, una sola vez.
    Y que las dimensiones sean correctas (n x n).
    Retorna True si cumple, False si no.
    """
    es_valida = True  # Variable para controlar validez
    
    if not matriz or len(matriz) != tamano_matriz:
        es_valida = False
    else:
        maximo_valor_esperado = tamano_matriz * tamano_matriz
        frecuencia_numeros = [0] * (maximo_valor_esperado + 1)  # Índice 0 no se usa

        for fila in range(tamano_matriz):
            if not matriz[fila] or len(matriz[fila]) != tamano_matriz:
                es_valida = False
                break
            for columna in range(tamano_matriz):
                numero = matriz[fila][columna]
                if not (1 <= numero <= maximo_valor_esperado):
                    es_valida = False
                    break
                frecuencia_numeros[numero] += 1
            if not es_valida:
                break

        if es_valida:
            for numero_esperado in range(1, maximo_valor_esperado + 1):
                if frecuencia_numeros[numero_esperado] != 1:
                    es_valida = False
                    break

    return es_valida


def es_cuadrado_magico(matriz, tamano_matriz):
    """
    Determina si la matriz es un cuadrado mágico.
    Retorna True si lo es, False si no.
    """
    es_magico = True  # Variable bandera para el resultado

    if not verificar_definicion_numeros(matriz, tamano_matriz):
        es_magico = False
    else:
        constante_magica = calcular_constante_magica(tamano_matriz)

        # Sumas de filas
        for fila in range(tamano_matriz):
            suma_fila = 0
            for columna in range(tamano_matriz):
                suma_fila += matriz[fila][columna]
            if suma_fila != constante_magica:
                es_magico = False
                break

        # Sumas de columnas (solo si sigue siendo mágico)
        if es_magico:
            for columna in range(tamano_matriz):
                suma_columna = 0
                for fila in range(tamano_matriz):
                    suma_columna += matriz[fila][columna]
                if suma_columna != constante_magica:
                    es_magico = False
                    break

        # Suma diagonal principal (solo si sigue siendo mágico)
        if es_magico:
            suma_diagonal_principal = 0
            for indice in range(tamano_matriz):
                suma_diagonal_principal += matriz[indice][indice]
            if suma_diagonal_principal != constante_magica:
                es_magico = False

        # Suma diagonal secundaria (solo si sigue siendo mágico)
        if es_magico:
            suma_diagonal_secundaria = 0
            for indice in range(tamano_matriz):
                suma_diagonal_secundaria += matriz[indice][tamano_matriz - 1 - indice]
            if suma_diagonal_secundaria != constante_magica:
                es_magico = False

    return es_magico


def main():
    print("--- Verificador de Cuadrado Mágico (Ultra Simplificado) ---")
    tamano_matriz = obtener_tamano_matriz()

    matriz_usuario = ingresar_matriz_manualmente(tamano_matriz)

    mostrar_matriz_simple(matriz_usuario)

    if es_cuadrado_magico(matriz_usuario, tamano_matriz):
        print("Resultado: La matriz ES un cuadrado mágico.")
    else:
        print("Resultado: La matriz NO es un cuadrado mágico.")


main()