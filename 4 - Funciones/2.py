# Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

def retornar_flotante() -> float:
    numero = float(input("Ingrese un número flotante: "))
    return numero

numero_ingresado = retornar_flotante()
print(numero_ingresado)