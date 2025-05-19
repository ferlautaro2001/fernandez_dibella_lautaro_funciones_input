# Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.

ingresos = 0
acumulados = 0
continuar = "si"

while continuar == "si":
    numero = int(input("Ingrese un número: "))
    acumulados += numero
    ingresos += 1
    
    if ingresos >= 5:
        respuesta = input("¿Desea seguir ingresando números? (si/no): ").lower()
        if respuesta == "no":
            continuar = "no"

print("La suma total de los números es:", acumulados)
print("El promedio es:", acumulados / ingresos)

