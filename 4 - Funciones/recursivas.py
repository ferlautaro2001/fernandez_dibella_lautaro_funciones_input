def sumar_digitos(numero: int) -> int:
    """
    Calcula la suma de los dígitos de un número de forma recursiva.
    
    Args:
        numero: El número entero cuyos dígitos se sumarán
        
    Returns:
        La suma de los dígitos del número
    """
    if numero < 10:
        return numero
    
    ultimo_digito = numero % 10
    resto_numero = numero // 10
    
    return ultimo_digito + sumar_digitos(resto_numero)


print(f"Suma de dígitos de 123: {sumar_digitos(123)}")  # 1+2+3 = 6
