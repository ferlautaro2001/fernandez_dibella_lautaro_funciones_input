from Input import get_int, get_float, get_string

if __name__ == "__main__":
    print("--- Probando get_int ---")
    edad = get_int(
        mensaje="Por favor, ingrese su edad.",
        mensaje_error="Error: la edad debe ser un número entre 18 y 99.",
        minimo=18,
        maximo=99,
        reintentos=2
    )
    if edad is not None:
        print(f"Edad ingresada: {edad}")
    else:
        print("No se pudo obtener una edad válida.")

    print("\n--- Probando get_float ---")
    altura = get_float(
        mensaje="Por favor, ingrese su altura en metros (ej: 1.75).",
        mensaje_error="Error: la altura debe ser un número entre 0.5 y 2.5.",
        minimo=0.5,
        maximo=2.5,
        reintentos=1
    )
    if altura is not None:
        print(f"Altura ingresada: {altura} m")
    else:
        print("No se pudo obtener una altura válida.")

    print("\n--- Probando get_string ---")
    codigo_postal = get_string(
        mensaje="Por favor, ingrese su código postal (exactamente 4 caracteres).",
        mensaje_error="Error: el código postal debe tener exactamente 4 caracteres.",
        longitud=4,
        reintentos=2
    )
    if codigo_postal is not None:
        print(f"Código postal ingresado: {codigo_postal}")
    else:
        print("No se pudo obtener un código postal válido.")