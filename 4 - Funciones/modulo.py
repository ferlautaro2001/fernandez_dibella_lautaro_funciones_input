def calcular_potencia(base: int, exponente: int) -> int:
    """
    Calcula la potencia de un número de forma recursiva.
    
    Args:
        base: El número base.
        exponente: El exponente al que se elevará la base.
        
    Returns:
        resultado: El resultado de elevar la base al exponente.
    """
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        resultado = 1
    else:
        # Caso recursivo: base * (base^exponente-1)
        resultado = base * calcular_potencia(base, exponente - 1)

    return resultado

print(f"2^9 = {calcular_potencia(2,9)}")  