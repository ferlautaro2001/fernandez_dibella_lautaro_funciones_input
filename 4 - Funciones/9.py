# Diseña una función que calcule la potencia de un número. La función debe recibir la base y el
# exponente como argumentos y devolver el resultado.

from math import pow

def potenciar(base:float,exponente:float)->float:
    resultado = pow(base,exponente)

    return resultado

x = potenciar(2,4)

print(x)


