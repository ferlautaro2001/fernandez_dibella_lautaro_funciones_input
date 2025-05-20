# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.

seguir = "si"
positivos = 0
negativos = 1

while seguir == "si":

    numero = int(input("Ingrese un número: "))

    if numero > 0:
        positivos += numero
    elif numero < 0:
        negativos *= numero
    else:
        print("Numero ingresado inválido")
        
    seguir = str(input("Desea seguir? si/no: ")).lower()

print("La sumatoria de los positivos es: ", positivos)
print("El producto de los negativos es: ", negativos)

