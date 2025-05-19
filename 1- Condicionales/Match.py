# Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
# En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 

# Si es invierno: solo se viaja a Bariloche.
# Si es verano: se viaja a Mar del plata y Cataratas.
# Si es otoño: se viaja a todos los lugares.
# Si es primavera: se viaja a todos los lugares menos Bariloche.

# Entrada.

estacion = input("Ingrese época del año (Invierno, Verano, Otoño, Primavera): ").strip().lower()

destino = input("Ingrese destino (Bariloche, Mar del Plata, Cataratas): ").strip().lower() 

match estacion:
    case "invierno":
        if destino == "bariloche":
            print("Se viaja")
        else:
            print("No se viaja")
    case "verano":
        if destino == "mar del plata" or destino == "cataratas":
            print("Se viaja")
        else:
            print("No se viaja")
    case "otoño":
        if destino != "":
            print("Se viaja")
        else:
            print("No se viaja")
    case "primavera":
        if destino != "bariloche":
            print("Se viaja")
        else:
            print("No se viaja")
    case _:
        print("Estación no válida.")
