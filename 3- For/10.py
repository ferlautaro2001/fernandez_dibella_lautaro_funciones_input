# 10.Ingresar un número. Determinar si el número es primo o no.

numero_ingresado = int(input("Ingresa un número para verificar si es primo: "))
divisor = 0
contador = 0

for contador in range(1, numero_ingresado + 1):
    if numero_ingresado % contador == 0:
        divisor += 1  # Incrementamos el contador de divisores

if divisor == 2:
    print(f"{numero_ingresado} es primo")
else:
    print(f"{numero_ingresado} no es primo")