# Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.

clave_correcta = "secreta123"
clave_ingresada = ""
intentos = 0

while clave_ingresada != clave_correcta:

    clave_ingresada = input("Ingrese clave: ")
    
    if clave_ingresada != clave_correcta:
        print("Clave errónea, intente de nuevo: ")
    intentos += 1   

print("Clave correcta")

