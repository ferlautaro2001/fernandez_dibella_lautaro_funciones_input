# Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.

def encontrar_posiciones_maximo(lista: list) -> list:

    # Paso 1: Encontrar el valor máximo
    maximo = 0
    for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]

    # Paso 2: Construir la lista de posiciones.
    posiciones = []
    for i in range(len(lista)):
        if lista[i] == maximo:
            posiciones += [i]  

    print(posiciones)

# Ejemplo.
lista_ejemplo = [1, 5, 10, 3, 10]
encontrar_posiciones_maximo(lista_ejemplo)
