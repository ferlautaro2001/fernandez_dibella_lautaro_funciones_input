# Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.

def obtener_positivos(lista: list) -> list:
    positivos = []

    for i in range(len(lista)):
        if lista[i] > 0:
            positivos += [lista[i]]  

    return positivos

def calcular_promedio_positivos(lista_numeros: list) -> float:
    """
    Calcula el promedio de una lista de números enteros.

    Args:
        lista_numeros (list): Una lista de números enteros.

    Returns:
        float: El promedio de los números en la lista.
            Retorna 0.0 si la lista está vacía para evitar división por cero.
    """
    suma_total = 0
    cantidad_elementos = obtener_positivos(lista_numeros)

    for i in range(len(cantidad_elementos)):                
        suma_total += cantidad_elementos[i]

    promedio = suma_total / len(cantidad_elementos)   

    return promedio


numeros_ejemplo = [-10, 20, -30, 40, 50]
promedio_ejemplo = calcular_promedio_positivos(numeros_ejemplo)
print(f"El promedio de los positivos es: {promedio_ejemplo}") 