#Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:

# 6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
# 4 y 5                ---> Aprobado, la nota es ...
# 1, 2 y 3            ---> Desaprobado, la nota es ...


nota = int(input("Ingrese calificación del 1 al 10: "))

if 6 <= nota <= 10:
    print("Promoción directa")
elif 4 <= nota <= 5:
    print("Aprobado")
elif 1 <= nota <= 3:
    print("Desaprobado")
else:
    print("Monto ingresado inválido")