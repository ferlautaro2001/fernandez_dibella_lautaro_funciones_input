from Input import get_int 

def sumar_digitos(numero: int) -> int:
    """
    Calcula la suma de los dígitos de un número entero no negativo
    de forma recursiva.

    Args:
        numero (int): El número entero no negativo cuyos dígitos se sumarán.

    Returns:
        int: La suma de los dígitos del número.
    """
    resultado_final = 0 # Variable para almacenar el resultado
    # Caso Base: Si el número tiene un solo dígito (0-9), la suma es el número mismo.
    if numero // 10 == 0: # Esto cubre números de 0 a 9
        resultado_final = numero
    # Paso Recursivo:
    # Suma el último dígito (numero % 10) con la suma de los dígitos restantes (numero // 10).
    else:
        resultado_final = (numero % 10) + sumar_digitos(numero // 10)
    
    return resultado_final # Único punto de retorno

# --- Programa Principal ---
if __name__ == "__main__":
    print("Suma de los dígitos de un número usando recursividad.")

    # Obtener el número del usuario usando get_int
    # El número debe ser no negativo para esta implementación.
    numero_ingresado = get_int(
        mensaje="Ingrese un número entero no negativo para sumar sus dígitos:",
        mensaje_error="Error: El número debe ser un entero válido y no negativo.",
        minimo=0,      # El número puede ser 0 o positivo
        maximo=1000000, # Un límite superior razonable para el ejemplo
        reintentos=2
    )

if numero_ingresado is not None:
    # Calcular y mostrar la suma de los dígitos
    resultado_suma_digitos = sumar_digitos(numero_ingresado)
    print(f"La suma de los dígitos de {numero_ingresado} es: {resultado_suma_digitos}")
else:
    print("No se pudo obtener un número válido.")