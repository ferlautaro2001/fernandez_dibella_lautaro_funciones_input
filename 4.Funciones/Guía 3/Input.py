import Validate 

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    """
    Solicita un número entero al usuario, validando que esté en un rango
    y permitiendo un número específico de reintentos para errores de rango.

    Args:
        mensaje: El mensaje que se muestra al usuario antes de pedir el dato.
        mensaje_error: Mensaje de error si el dato es inválido (fuera de rango).
        minimo: Valor mínimo admitido (inclusive).
        maximo: Valor máximo admitido (inclusive).
        reintentos: Cantidad de veces que se volverá a pedir el dato en caso de error de rango.

    Returns:
        int | None: El número entero validado, o None si se agotan los reintentos.
                    NOTA: Si el usuario ingresa un valor no convertible a entero (ej: "abc"),
                    el programa fallará con ValueError en la línea de conversión int().
    """
    print(mensaje)
    numero_validado = None

    for intento_actual in range(reintentos + 1): # Un intento inicial + 'reintentos' adicionales
        entrada_usuario = input("Ingrese el número entero: ")

        # Conversión directa a entero.
        # Si 'entrada_usuario' no es una cadena numérica válida para int(),
        # la siguiente línea CAUSARÁ UN ValueError Y EL PROGRAMA SE DETENDRÁ.
        valor_actual_int = int(entrada_usuario)

        # Validación de rango usando la función de Validate.py
        if Validate.validate_number(valor_actual_int, minimo, maximo):
            numero_validado = valor_actual_int
            break  # Número válido encontrado, salir del bucle de reintentos
        else:
            # Error de rango (la conversión a int fue exitosa)
            print(mensaje_error)
            # Si este fue el último intento permitido (intento_actual == reintentos),
            # el bucle terminará y se retornará numero_validado (que sería None si nunca se validó).
            if intento_actual == reintentos:
                print("Se han agotado los reintentos para el ingreso dentro del rango.")


    return numero_validado


def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float | None:
    """
    Solicita un número flotante al usuario, validando que esté en un rango
    y permitiendo un número específico de reintentos para errores de rango.

    Args:
        mensaje: El mensaje que se muestra al usuario antes de pedir el dato.
        mensaje_error: Mensaje de error si el dato es inválido (fuera de rango).
        minimo: Valor mínimo admitido (inclusive).
        maximo: Valor máximo admitido (inclusive).
        reintentos: Cantidad de veces que se volverá a pedir el dato en caso de error de rango.

    Returns:
        float | None: El número flotante validado, o None si se agotan los reintentos.
                        NOTA: Si el usuario ingresa un valor no convertible a flotante (ej: "abc"),
                        el programa fallará con ValueError en la línea de conversión float().
    """
    print(mensaje)
    numero_validado = None

    for intento_actual in range(reintentos + 1):
        entrada_usuario = input("Ingrese el número decimal: ")
        
        # Conversión directa a flotante.
        # Si 'entrada_usuario' no es una cadena numérica válida para float(),
        # la siguiente línea CAUSARÁ UN ValueError Y EL PROGRAMA SE DETENDRÁ.
        valor_actual_float = float(entrada_usuario)

        if Validate.validate_number(valor_actual_float, minimo, maximo):
            numero_validado = valor_actual_float
            break
        else:
            print(mensaje_error)
            if intento_actual == reintentos:
                print("Se han agotado los reintentos para el ingreso dentro del rango.")
                
    return numero_validado


def get_string(mensaje: str, mensaje_error: str, longitud: int, reintentos: int) -> str | None:
    """
    Solicita una cadena de texto al usuario, validando su longitud
    y permitiendo un número específico de reintentos.

    Args:
        mensaje: El mensaje que se muestra al usuario antes de pedir el dato.
        mensaje_error: Mensaje de error si la longitud de la cadena es incorrecta.
        longitud: La longitud exacta que debe tener la cadena.
        reintentos: Cantidad de veces que se volverá a pedir el dato en caso de error.

    Returns:
        str | None: La cadena de texto validada, o None si se agotan los reintentos.
    """
    print(mensaje)
    texto_validado = None

    for intento_actual in range(reintentos + 1):
        entrada_usuario = input("Ingrese el texto: ")

        if Validate.validate_length(entrada_usuario, longitud):
            texto_validado = entrada_usuario
            break
        else:
            print(mensaje_error)
            if intento_actual == reintentos:
                print("Se han agotado los reintentos para el ingreso con la longitud correcta.")
                
    return texto_validado