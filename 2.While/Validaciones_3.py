# Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.

nota_valida = False
nota_ingresada = 0

while nota_valida == False:
    nota_ingresada = int(input("Ingrese una nota entre el 1 y el 10: "))
    
    if nota_ingresada >= 1 and nota_ingresada <= 10:
        print("Nota válida")
        nota_valida = True
    else:

        print("Nota inválida, intente otra vez")