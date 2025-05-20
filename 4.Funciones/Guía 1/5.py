#Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
from math import pi , pow

radio = int(input("ingrese su radio "))

def calcular_area_circulo(radio: float|int )->float:
    """Función que retorna el area de un círculo. 

    Args:
        radio (float | int): Radio. Se debe ingresar un número entero o flotante.

    Returns:
        area: Retorna un numero float dependiendo del radio ingresado, este será igual al area.
    """

    area = None
    if (type(radio) == float or type(radio) == int) and radio > 0:
        radio_al_cuadrado = pow(radio,2)
        area = pi * radio_al_cuadrado 

    return area

area = calcular_area_circulo(radio)

print(area)