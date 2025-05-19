def validate_number(numero: int | float, minimo: int | float, maximo: int | float) -> bool:
    """
    Valida si un número se encuentra dentro de un rango específico (inclusive).

    Args:
        numero: El número a validar (ya convertido a int o float).
        minimo: El valor mínimo permitido del rango.
        maximo: El valor máximo permitido del rango.

    Returns:
        bool: True si el número está dentro del rango, False en caso contrario.
    """
    return minimo <= numero <= maximo

def validate_length(texto: str, longitud_deseada: int) -> bool:
    """
    Valida si la longitud de una cadena de texto es igual a una longitud específica.

    Args:
        texto: La cadena de texto a validar.
        longitud_deseada: La longitud que debe tener la cadena.

    Returns:
        bool: True si la longitud de la cadena es la deseada, False en caso contrario.
    """
    return len(texto) == longitud_deseada