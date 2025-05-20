# Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:

# La suma acumulada de los números negativos.
# La suma acumulada de los números positivos.
# La cantidad de números negativos ingresados.
# El promedio de los números positivos.
# El número positivo más grande.
# El porcentaje de números negativos ingresados, respecto del total de ingresos.

vuelta_uno = False

negativos = 0  # Suma acumulada de números negativos
positivos = 0  # Suma acumulada de números positivos
iteracion_negativa = 0  # Cantidad de números negativos
iteracion_positiva = 0  # Cantidad de números positivos
maximo_positivo = None  # Número positivo más grande
total_vueltas = 0  # Total de números ingresados

while not vuelta_uno:
    seguir = input("¿Desea ingresar un número? (si/no): ").lower()

    if seguir == "si":
        numero = int(input("Ingrese un número: "))
        total_vueltas += 1
        if numero < 0:
            negativos += numero
            iteracion_negativa += 1
        elif numero > 0:
            positivos += numero
            iteracion_positiva += 1
            if maximo_positivo is None or numero > maximo_positivo:
                maximo_positivo = numero
    elif seguir == "no":
        vuelta_uno = True
    else:
        print("Respuesta inválida. Ingrese 'si' o 'no'.")

# Calcular promedio de positivos y porcentaje de negativos
promedio_positivos = 0
if iteracion_positiva > 0:
    promedio_positivos = positivos / iteracion_positiva

porcentaje_negativos = 0
if total_vueltas > 0:
    porcentaje_negativos = (iteracion_negativa / total_vueltas) * 100

# Mostrar resultados
print("\nResultados:")
print(f"Suma acumulada de números negativos: {negativos}")
print(f"Suma acumulada de números positivos: {positivos}")
print(f"Cantidad de números negativos ingresados: {iteracion_negativa}")
print(f"Promedio de números positivos: {promedio_positivos}")
print(f"Número positivo más grande: {maximo_positivo if maximo_positivo is not None else 'No se ingresaron números positivos'}")
print(f"Porcentaje de números negativos: {porcentaje_negativos}%")