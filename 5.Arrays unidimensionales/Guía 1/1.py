# Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.

def crear_array(longitud: int) -> list:
    """
    Crea una lista (array) de números.
    La lista contendrá números desde 0 hasta longitud - 1.

    Args:
        longitud (int): La cantidad de elementos que tendrá la lista.

    Returns:
        array: Una lista de números enteros.
    """
    array = []

    for i in range(longitud):
        array += [i]

    return array


