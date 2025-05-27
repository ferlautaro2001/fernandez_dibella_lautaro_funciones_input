# Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.
from numero1 import crear_array

def crear_custom(cantidad_numeros: int) -> list:
    """
    Crea una lista y la puebla con números ingresados por el usuario.
    Primero crea una lista de un tamaño determinado y luego reemplaza
    cada uno de sus elementos con la entrada del usuario.

    Args:
        cantidad_numeros (int): La cantidad de números que se le solicitarán al usuario.

    Returns:
        array_base: Una lista con los números que el usuario ingresó.
    """

    array_base = crear_array(cantidad_numeros)

    for i in range(cantidad_numeros):
        numero_ingresado = int(input(f"Ingrese el número para la posición {i}: "))
        array_base[i] = numero_ingresado
        
    return array_base

array_base = crear_custom(5)
print(array_base)
