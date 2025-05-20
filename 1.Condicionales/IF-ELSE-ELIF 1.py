# A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Aleros
# 200 cm o más: Ala-Pívot o Pívot


altura = float(input("Ingrese la altura en cm: ")) 

if altura < 160:
    print("Base")
elif 160 <= altura <= 179:  
    print("Escolta")
elif 180 <= altura <= 199:
    print ("Alero")
elif altura >= 200:        
    print("Pivot")
else:                      
    print("No clasificado")

