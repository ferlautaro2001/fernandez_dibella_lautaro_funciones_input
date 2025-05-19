# Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se
# ingresa el numero 5, la salida del programa será la siguiente: 1 12 123 1234 12345

numero_filas = int(input("Ingrese un número para la altura de la pirámide: "))

for fila_actual in range(1, numero_filas + 1):
    linea = ""
    for numero_a_imprimir in range(1, fila_actual + 1):
        linea += str(numero_a_imprimir)
    print(linea)
