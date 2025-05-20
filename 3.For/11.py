# Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número
# ingresado. Informar cuántos números primos se encontraron.

contador_primos = 0

numero_ingresado = int(input("Ingresa un número: "))

for numero in range(1, numero_ingresado + 1):
    # Contar los divisores del número actual.
    divisor = 0
    for contador in range(1, numero + 1):
        if numero % contador == 0:
            divisor += 1
    # Si tiene exactamente 2 divisores, es primo.
    if divisor == 2:
        print(numero)
        contador_primos += 1


print(f"Se encontraron {contador_primos} números primos.")
print(f"Números primos entre 1 y {numero_ingresado}:")