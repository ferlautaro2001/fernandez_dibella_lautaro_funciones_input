# Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.

correcto = False

while correcto == False:
    color = input("Ingrese un color: ").lower()

    if color == "rojo" or color == "verde" or color == "azul":
        correcto = True
        print("Color válido")
    else:
        print("Color inválido, intente de nuevo")
