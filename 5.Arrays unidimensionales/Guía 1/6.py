# Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.

def encontrar_maximo(lista:list ) -> int:
    maximo=0
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    
    posicion = []
    
    for i in range (len(lista)):
        if lista[i] == maximo:
            posicion += [i]

    return posicion

lista_ejemplo =  [1, 5, 10]
posicion = encontrar_maximo(lista_ejemplo)
print(posicion)

