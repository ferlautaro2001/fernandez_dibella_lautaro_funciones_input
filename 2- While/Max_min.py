maximo = 0
minimo = 0
seguir = "si"
bandera_primer_ingreso = False

while seguir == "si":
    numero = float(input("Ingrese un numero: "))

    if numero > maximo or bandera_primer_ingreso == False:
        maximo = numero
    
    if numero < minimo or bandera_primer_ingreso == False:
        minimo = numero
        
        bandera_primer_ingreso = True
    
    seguir = input("Seguir? ")