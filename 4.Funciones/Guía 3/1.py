from Input import get_int 

def sumar_naturales(numero: int) -> int:
    """
    Calcula la suma de los primeros 'numero' números naturales de forma recursiva.
    Ej: Si numero es 4, calcula 1 + 2 + 3 + 4 = 10.

    Args:
        numero (int): Un entero positivo que indica hasta qué número natural sumar.

    Returns:
        int: La suma de los primeros 'numero' números naturales.
            Retorna 0 si el número es 0 o negativo.
    """
    resultado_final = 0 # Variable para almacenar el resultado
    # Caso Base:
    if numero <= 0:
        resultado_final = 0
    elif numero == 1:
        resultado_final = 1
    # Paso Recursivo:
    else:
        resultado_final = numero + sumar_naturales(numero - 1)
    
    return resultado_final # Único punto de retorno

if __name__ == "__main__":
    print("Cálculo de la suma de los primeros N números naturales.")

    numero_ingresado = get_int(
        mensaje="Ingrese un número entero positivo para calcular la suma de los naturales:",
        mensaje_error="Error: El número debe ser un entero positivo y estar en el rango permitido.",
        minimo=1,      # Para la suma de naturales, usualmente n >= 1
        maximo=100,    # Un límite superior razonable para evitar recursión muy profunda en ejemplos
        reintentos=2   # Número de reintentos permitidos por get_int
    )

if numero_ingresado is not None: # Esta indentación estaba incorrecta en el archivo original
    resultado_suma = sumar_naturales(numero_ingresado)
    print(f"La suma de los primeros {numero_ingresado} números naturales es: {resultado_suma}")
else:
    print("No se pudo obtener un número válido para calcular la suma.")