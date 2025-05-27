def calcular_constante_magica(n: int) -> int:
    """
    Calcula la constante mágica M para un cuadrado de orden n.
    """
    m_resultado = n * (n**2 + 1) // 2
    return m_resultado 

def sumar_fila(matriz: list, num_fila: int) -> int:
    """Suma los elementos de una fila específica de la matriz."""
    suma_resultado = 0
    fila = matriz[num_fila]
    for i in range(len(fila)):
        suma_resultado += fila[i]
    return suma_resultado 

def sumar_columna(matriz: list, num_columna: int, n: int) -> int:
    """Suma los elementos de una columna específica de la matriz."""
    suma_resultado = 0
    for i in range(n): 
        suma_resultado += matriz[i][num_columna]
    return suma_resultado 

def sumar_diagonal_principal(matriz: list, n: int) -> int:
    """Suma los elementos de la diagonal principal."""
    suma_resultado = 0
    for i in range(n):
        suma_resultado += matriz[i][i]
    return suma_resultado 

def sumar_diagonal_secundaria(matriz: list, n: int) -> int:
    """Suma los elementos de la diagonal secundaria."""
    suma_resultado = 0
    for i in range(n):
        suma_resultado += matriz[i][n - 1 - i]
    return suma_resultado 

def mostrar_matriz_formato(matriz: list, n: int) -> None:
    """Muestra la matriz en un formato legible."""
    print("\n--- Matriz Ingresada ---")
    for i in range(n):
        fila_str = ""
        for j in range(n):
            fila_str += f"{matriz[i][j]:4} " 
        print(fila_str)
    return None 