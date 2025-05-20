# Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def retornar() -> int: 
    numero = int(input("Ingrese un número entero: "))
    return numero

pedir_numero = retornar()  
print(pedir_numero)