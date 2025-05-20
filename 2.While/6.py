# 6) # Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números ingresados y el promedio de los mismos.

seguir = "si"
vueltas = 0
total_numeros = 0

while seguir == "si":

    numero = int(input("Ingrese un número: "))
    seguir = str(input("Desea seguir? si/no: ")).lower()
    total_numeros += numero
    vueltas += 1

print("La suma total es: ", total_numeros)
print("El promedio es: ", total_numeros/vueltas)


