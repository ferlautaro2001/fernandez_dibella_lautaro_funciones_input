# Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. 


def calcular_promedio(lista_numeros: list) -> float:
    """
    Calcula el promedio de una lista de números enteros.

    Args:
        lista_numeros (list): Una lista de números enteros.

    Returns:
        float: El promedio de los números en la lista.
               Retorna 0.0 si la lista está vacía para evitar división por cero.
    """
    suma_total = 0
    cantidad_elementos = len(lista_numeros)

    if cantidad_elementos > 0:

        for i in range(len(lista_numeros)):                
            suma_total += lista_numeros[i]
        promedio = suma_total / cantidad_elementos

    else:

        promedio = 0.0
        
    return promedio

numeros_ejemplo = [10, 20, 30, 40, 50]
promedio_ejemplo = calcular_promedio(numeros_ejemplo)
print(f"La lista es: {numeros_ejemplo}")
print(f"El promedio de los números es: {promedio_ejemplo}") # Salida esperada: 30.0