from Input import get_int 

def fibonacci(numero: int) -> int:
    """
    Calcula el n-ésimo término de la sucesión de Fibonacci de forma recursiva.
    La sucesión se considera como F(0)=0, F(1)=1, F(2)=1, F(3)=2, ...

    Args:
        numero (int): El índice (n) del término de Fibonacci a calcular (debe ser >= 0).

    Returns:
        int: El n-ésimo término de la sucesión de Fibonacci.
    """
    resultado_final = 0 # Variable para almacenar el resultado
    # Casos Base:
    if numero == 0:
        resultado_final = 0
    elif numero == 1:
        resultado_final = 1
    # Paso Recursivo:
    # F(n) = F(n-1) + F(n-2) para n > 1
    else:
        resultado_final = fibonacci(numero - 1) + fibonacci(numero - 2)
    
    return resultado_final # Único punto de retorno

# --- Programa Principal ---
if __name__ == "__main__":
    print("Cálculo del n-ésimo término de la sucesión de Fibonacci usando recursividad.")

    # Obtener el índice 'n' del usuario usando get_int
    # El índice debe ser no negativo.
    n_termino = get_int(
        mensaje="Ingrese el índice 'n' del término de Fibonacci a calcular (entero >= 0):",
        mensaje_error="Error: El índice debe ser un entero válido y no negativo.",
        minimo=0,      # Fibonacci se define para n >= 0
        maximo=30,     # Límite superior para evitar tiempos de ejecución muy largos
                    # y recursión muy profunda con esta implementación simple.
        reintentos=2
    )

if n_termino is not None:
    # Calcular y mostrar el término de Fibonacci
    resultado_fibonacci = fibonacci(n_termino)
    print(f"El término F({n_termino}) de la sucesión de Fibonacci es: {resultado_fibonacci}")
else:
    print("No se pudo obtener un índice válido.")