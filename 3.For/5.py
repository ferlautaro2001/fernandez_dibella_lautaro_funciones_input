# Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0.
# Mostrar la suma y el promedio de todos los números.

contador = 0
vueltas = 0
acumulador = 0

for contador in range (1, 11):
    numero = int(input("Ingrese un número: "))

    if numero == 0:
        break
    elif numero !=0:
        acumulador += numero
    vueltas += 1

print(f"La suma de los números ingresados es: {acumulador}\nEl promedio es: {acumulador/vueltas}")            


