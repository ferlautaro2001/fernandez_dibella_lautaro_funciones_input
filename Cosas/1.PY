usuario = False

def rango():
    usuario = str(input("Desea cambiar el parametro del 1 al 10?: "))
    if usuario == "si":
        bajo = int(input("Determine su limite mas bajo: "))
        alto = int(input("Determine su limite mas alto: "))
    else:
        bajo = 1
        alto = 10
    return bajo, alto

bajo, alto = rango()

def multiplicacion (bajo, alto):
    numero = int(input("Ingrese el numero que quiera multiplicar: "))
    for i in range(bajo, alto + 1):
        print(i, "x", numero, "=", numero * i) 

multiplicacion(bajo, alto)