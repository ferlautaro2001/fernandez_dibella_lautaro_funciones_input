# Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.

def tabla_de_multiplicar(numero, inicio=1, fin=10):
    """
    Imprime la tabla de multiplicar de un número dado dentro de un rango específico.

    Args:
        numero: El número para el cual se generará la tabla de multiplicar.
        inicio: (Opcional) El número inicial del rango de multiplicación.
                Por defecto es 1.
        fin: (Opcional) El número final del rango de multiplicación.
            Por defecto es 10.
    """
    print(f"Tabla de multiplicar del {numero} (del {inicio} al {fin}):")
    for i in range(inicio, fin + 1):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Ejemplos de uso:

# Tabla del 5 (por defecto, del 1 al 10)
tabla_de_multiplicar(5)

# Tabla del 7, del 3 al 8
tabla_de_multiplicar(7, 3, 8)

# Tabla del 3, solo hasta el 5 (inicio por defecto es 1)
tabla_de_multiplicar(3, fin=5)

# Tabla del 9, empezando desde el 5 (fin por defecto es 10)
tabla_de_multiplicar(9, inicio=5)

# Tabla del 12, del 10 al 15
tabla_de_multiplicar(12, 10, 15)