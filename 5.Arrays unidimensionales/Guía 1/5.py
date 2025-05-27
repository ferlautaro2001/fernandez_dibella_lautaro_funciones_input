# Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.
lista_ejemplo = [1,2,3,4,5]

def multiplicar(lista: list) -> int:

    resultado = 1
    for i in range (len(lista)):
        resultado *= lista[i]
    return resultado

resultado = multiplicar(lista_ejemplo)
print(resultado)
