# 4) # Mostrar la suma de los números pares desde el 1 hasta el 10.

contador = 1 # Contador inicializado en 1. 
acumulador = 0 # Acumulador inicializado en 0. 

while contador <= 10: # Condición. 
    if contador % 2 == 0: # Si el resto de la divisón por dos de contador es distinto de 0. 
        acumulador += contador # Guardo ese valor de contador en mi acumulador. 
    contador += 1 # Sumo una vuelta al contador. 
print(acumulador) # Imprimo mi valor total final. (Suma de todos los valores que cumplen.)