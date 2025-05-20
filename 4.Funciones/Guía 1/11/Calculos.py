def calcular_primos(numero)->int:
    contador_primos = 0
    for i in range(1, numero + 1):
        # Contar los divisores del número actual.
        divisor = 0
        for j in range(1, i + 1):
            if i % j == 0:
                divisor += 1
        # Si tiene exactamente 2 divisores, es primo.
        if divisor == 2:
            print(i)
            contador_primos += 1

    resultado = print(f"Números primos entre 1 y {numero} es {contador_primos}:")
    return resultado



