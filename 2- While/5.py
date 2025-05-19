# 5) Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.

vueltas = 1 # Inicializo vueltas en 1 como contador para controlar el ciclo.
acumulador = 0 # Inicializo acumulador en 0 para acumular la suma de los números
contador = 0 # Inicializo contador en 0 para contar la cantidad de números ingresados

while vueltas <= 5: # Mientras las vueltas sean menores o iguales a 5.

    num = int(input("Ingrese un número: ")) # Solicito ingresar un número y lo guardo en num.

    acumulador += num # Agrego el número ingresado a mi acumulador. 

    contador += 1 # Incremento el contador en 1 por cada número ingresado.

    vueltas += 1 # Incremento vueltas en 1 por cada vuelta. 

print("La suma es:", acumulador) # Imprimo el total. 
print("El promedio es:", acumulador / contador) # Imprimo el promedio.