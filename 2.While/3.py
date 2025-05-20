# 3) # Mostrar la suma de los números desde el 1 hasta el 10.

contador = 1 # Contador.

acumulador = 0 # Acumulador. 

while contador <= 10: # Condición.(Mientras contador sea menor o igual a 10 ejecuto una orden)
    acumulador += contador  # Acumulo el valor de contador dentro de "acumulador".
    contador += 1 # Incremento contador en cada iteración del bucle while.
    print(acumulador) # Imprimo el valor de lo acumulado en cada iteración del bucle while.
