def calcular_potencia(base: int, exponente: int) -> int:
    """
    Calcula la potencia de un número a partir de una base y un exponente.
    Realiza multiplicaciones sucesivas de la base, tantas veces como
    indique el exponente.

    Args:
        base (int): El número que se multiplicará.
        exponente (int): La cantidad de veces que se multiplicará la base.

    Returns:
        int: El resultado de la potencia.
    """
    # Se inicializa una variable como acumulador. 
    # Se usa el valor 1 porque es el elemento neutro de la multiplicación.
    resultado = 1

    # Si el exponente es 0, el resultado es 1 por definición matemática.
    # Si es mayor a 0, se entra al bucle.
    if exponente > 0:
        # Se utiliza un bucle 'for' para repetir la operación un número
        # determinado de veces (el valor del exponente). 
        for i in range(exponente):
            resultado = resultado * base

    # La función devuelve el valor acumulado en la variable 'resultado'. 
    return resultado

# --- Ejemplo de uso ---
# Se invoca la función para probarla.
base_ingresada = 2
exponente_ingresado = 5
resultado_final = calcular_potencia(base_ingresada, exponente_ingresado)

print(resultado_final)