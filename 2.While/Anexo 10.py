# Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.

ingresos = 0
acumulados = 0
MIN_NUMEROS = 5
MAX_NUMEROS = 10
continuar = "si"

while continuar == "si" and ingresos < MAX_NUMEROS:
    numero = int(input("Ingrese un número: "))
    acumulados += numero
    ingresos += 1
    
    if ingresos >= MIN_NUMEROS:
        respuesta = input(f"Ya ingresó {ingresos} números. ¿Desea seguir ingresando? (s/n): ").lower()
        if respuesta == "no":
            continuar = "no"

print("La suma total de los números es:", acumulados)
print("El promedio es:", acumulados / ingresos)