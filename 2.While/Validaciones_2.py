# Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.

clave_correcta = "secreta123"
clave_ingresada = ""
intentos = 0
max_intentos = 3

while intentos < max_intentos and clave_ingresada != clave_correcta:

    clave_ingresada = input("Ingrese clave: ")

    if clave_ingresada != clave_correcta:
        print("Clave errónea, intente de nuevo.")
    intentos += 1

if clave_ingresada == clave_correcta:
    print("Clave correcta")
else:
    print("Acceso bloqueado. Se excedieron los intentos.")