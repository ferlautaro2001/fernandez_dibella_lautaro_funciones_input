# Ingresar 10 números enteros. Determinar el máximo y el mínimo.

ingresos = 0
maximo = 0
minimo = 0

while ingresos < 10:

    numero = int(input("Ingrese un número: "))
    
    if numero > maximo:
        maximo = numero
    elif numero < minimo:
        minimo = numero

    ingresos += 1

print("El máximo es: ", maximo)
print("El mínimo es: ", minimo)
