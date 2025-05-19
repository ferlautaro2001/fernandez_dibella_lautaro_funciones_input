# Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:

	# 5 x 0 = 0
	# 5 x 1  = 5
	# 5 x 2 = 10
	# 5 x 3  = 15 …

numero = int(input("Ingrese un número: "))

for contador in range (1,11):
    print(numero*contador)																							