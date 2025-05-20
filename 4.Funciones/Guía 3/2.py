from Input import get_int 

def calcular_potencia(base: int, exponente: int) -> int:
    """
    Calcula la potencia de un número (base elevado a un exponente)
    de forma recursiva.
    Asume que el exponente es un entero no negativo.

    Args:
        base (int): El número base.
        exponente (int): El exponente (debe ser >= 0).

    Returns:
        int: El resultado de base^exponente.
    """
    resultado_final = 0 # Variable para almacenar el resultado
    # Caso Base: Cualquier número elevado a 0 es 1.
    if exponente == 0:
        resultado_final = 1
    # Paso Recursivo: base^exponente = base * base^(exponente-1)
    else:
        resultado_final = base * calcular_potencia(base, exponente - 1)
    
    return resultado_final # Único punto de retorno

# --- Programa Principal ---
if __name__ == "__main__":
    print("Cálculo de potencia (base^exponente) usando recursividad.")

    # Obtener la base del usuario
    # No hay restricciones específicas para la base más allá de ser un entero.
    base_ingresada = get_int(
        mensaje="Ingrese el número base (entero):",
        mensaje_error="Error: La base debe ser un número entero válido.",
        minimo=-1000,  # Un rango amplio para la base
        maximo=1000,
        reintentos=2
    )

if base_ingresada is not None:
    # Obtener el exponente del usuario
    # El exponente debe ser no negativo para esta implementación simple.
    exponente_ingresado = get_int(
        mensaje="Ingrese el exponente (entero >= 0):",
        mensaje_error="Error: El exponente debe ser un entero válido y no negativo.",
        minimo=0,      # Exponente no negativo
        maximo=20,     # Límite para evitar números demasiado grandes y recursión excesiva
        reintentos=2
    )

if exponente_ingresado is not None:
    # Calcular y mostrar la potencia
    resultado_potencia = calcular_potencia(base_ingresada, exponente_ingresado)
    print(f"{base_ingresada}^{exponente_ingresado} = {resultado_potencia}")
else:
    print("No se pudo obtener un exponente válido.")
