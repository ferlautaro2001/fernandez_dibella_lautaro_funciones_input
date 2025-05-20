# 📌 Desafío: Encuesta Tecnológica en UTN Technologies
# UTN Technologies, una reconocida software factory, está en la búsqueda de ideas para su próximo desarrollo en Python, con el objetivo de revolucionar el mercado.
# Las tecnologías en evaluación son:
#  🔹 Inteligencia Artificial (IA)
#  🔹 Realidad Virtual/Aumentada (RV/RA)
#  🔹 Internet de las Cosas (IOT)
# Para tomar una decisión informada, la empresa ha lanzado una encuesta entre sus empleados con el propósito de analizar ciertas métricas.
# 🔹 Recolección de Datos
# Cada empleado encuestado deberá proporcionar la siguiente información:
#  ✔️ Nombre
#  ✔️ Edad (debe ser 18 años o más)
#  ✔️ Género (Masculino, Femenino, Otro)
#  ✔️ Tecnología elegida (IA, RV/RA, IOT)
# El sistema deberá permitir ingresar los datos de 10 empleados mediante la terminal.
# 🔹 Análisis de Datos
# A partir de las respuestas, se deben calcular las siguientes métricas:
# 1️⃣ Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive).
# 2️⃣ Porcentaje de empleados que NO votaron por IA, siempre y cuando:
# Su género no sea Femenino 
# Su edad está entre los 33 y 40 años.
# 3️⃣ Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.


# 🔹 Requisitos del Programa
#  ✔️ Los datos deben solicitarse y validarse correctamente.
#  ✔️ Utilizar variables adecuadas para almacenar la información y facilitar su análisis.
#  ✔️ Presentar los resultados de manera clara y organizada.


nombre1 = ""  
nombre2 = ""  
nombre3 = ""  
nombre4 = ""  
nombre5 = ""  
nombre6 = ""  
nombre7 = ""  
nombre8 = ""  
nombre9 = ""  
nombre10 = ""  
edad1 = 0  
edad2 = 0  
edad3 = 0  
edad4 = 0  
edad5 = 0  
edad6 = 0  
edad7 = 0  
edad8 = 0  
edad9 = 0  
edad10 = 0  
genero1 = ""  
genero2 = ""  
genero3 = ""  
genero4 = ""  
genero5 = ""  
genero6 = ""  
genero7 = ""  
genero8 = ""  
genero9 = ""  
genero10 = ""  
tecnologia1 = ""  
tecnologia2 = ""  
tecnologia3 = ""  
tecnologia4 = ""  
tecnologia5 = ""  
tecnologia6 = ""  
tecnologia7 = ""  
tecnologia8 = ""  
tecnologia9 = ""  
tecnologia10 = ""

# Variables para métricas
contador_iot_ia_masculino_25_50 = 0
contador_no_ia_no_femenino_33_40 = 0
contador_total_no_femenino_33_40 = 0
edad_max_masculino = 0
nombre_max_masculino = ""
tecnologia_max_masculino = ""

# Ingresar datos de los 10 empleados usando while
contador = 1
while contador <= 10:
    # Validar nombre
    nombre = ""
    while not nombre:
        nombre = input("Ingrese nombre del empleado " + str(contador) + ": ")
    if contador == 1:
        nombre1 = nombre
    if contador == 2:
        nombre2 = nombre
    if contador == 3:
        nombre3 = nombre
    if contador == 4:
        nombre4 = nombre
    if contador == 5:
        nombre5 = nombre
    if contador == 6:
        nombre6 = nombre
    if contador == 7:
        nombre7 = nombre
    if contador == 8:
        nombre8 = nombre
    if contador == 9:
        nombre9 = nombre
    if contador == 10:
        nombre10 = nombre

    # Validar edad
    edad = 0
    while not edad >= 18:
        edad = int(input("Ingrese edad del empleado " + str(contador) + " (18 o más): "))
        if not edad >= 18:
            print("Edad inválida. Debe ser 18 o más.")
    if contador == 1:
        edad1 = edad
    if contador == 2:
        edad2 = edad
    if contador == 3:
        edad3 = edad
    if contador == 4:
        edad4 = edad
    if contador == 5:
        edad5 = edad
    if contador == 6:
        edad6 = edad
    if contador == 7:
        edad7 = edad
    if contador == 8:
        edad8 = edad
    if contador == 9:
        edad9 = edad
    if contador == 10:
        edad10 = edad

    # Validar género
    genero = ""
    while not (genero == "masculino" or genero == "femenino" or genero == "otro"):
        genero = input("Ingrese género del empleado " + str(contador) + " (Masculino, Femenino, Otro): ").lower()
        if not (genero == "masculino" or genero == "femenino" or genero == "otro"):
            print("Género inválido. Debe ser Masculino, Femenino u Otro.")
    if contador == 1:
        genero1 = genero
    if contador == 2:
        genero2 = genero
    if contador == 3:
        genero3 = genero
    if contador == 4:
        genero4 = genero
    if contador == 5:
        genero5 = genero
    if contador == 6:
        genero6 = genero
    if contador == 7:
        genero7 = genero
    if contador == 8:
        genero8 = genero
    if contador == 9:
        genero9 = genero
    if contador == 10:
        genero10 = genero

    # Validar tecnología
    tecnologia = ""
    while not (tecnologia == "ia" or tecnologia == "rv/ra" or tecnologia == "iot"):
        tecnologia = input("Ingrese tecnología elegida por el empleado " + str(contador) + " (IA, RV/RA, IOT): ").lower()
        if not (tecnologia == "ia" or tecnologia == "rv/ra" or tecnologia == "iot"):
            print("Tecnología inválida. Debe ser IA, RV/RA o IOT.")
    if contador == 1:
        tecnologia1 = tecnologia
    if contador == 2:
        tecnologia2 = tecnologia
    if contador == 3:
        tecnologia3 = tecnologia
    if contador == 4:
        tecnologia4 = tecnologia
    if contador == 5:
        tecnologia5 = tecnologia
    if contador == 6:
        tecnologia6 = tecnologia
    if contador == 7:
        tecnologia7 = tecnologia
    if contador == 8:
        tecnologia8 = tecnologia
    if contador == 9:
        tecnologia9 = tecnologia
    if contador == 10:
        tecnologia10 = tecnologia

    contador += 1

# Calcular métricas usando while
contador = 1
while contador <= 10:
    # Seleccionar datos según el contador
    if contador == 1:
        nombre = nombre1
        edad = edad1
        genero = genero1
        tecnologia = tecnologia1
    if contador == 2:
        nombre = nombre2
        edad = edad2
        genero = genero2
        tecnologia = tecnologia2
    if contador == 3:
        nombre = nombre3
        edad = edad3
        genero = genero3
        tecnologia = tecnologia3
    if contador == 4:
        nombre = nombre4
        edad = edad4
        genero = genero4
        tecnologia = tecnologia4
    if contador == 5:
        nombre = nombre5
        edad = edad5
        genero = genero5
        tecnologia = tecnologia5
    if contador == 6:
        nombre = nombre6
        edad = edad6
        genero = genero6
        tecnologia = tecnologia6
    if contador == 7:
        nombre = nombre7
        edad = edad7
        genero = genero7
        tecnologia = tecnologia7
    if contador == 8:
        nombre = nombre8
        edad = edad8
        genero = genero8
        tecnologia = tecnologia8
    if contador == 9:
        nombre = nombre9
        edad = edad9
        genero = genero9
        tecnologia = tecnologia9
    if contador == 10:
        nombre = nombre10
        edad = edad10
        genero = genero10
        tecnologia = tecnologia10

    # Métrica 1: Empleados masculinos que votaron por IOT o IA, entre 25 y 50 años
    if genero == "masculino" and (tecnologia == "iot" or tecnologia == "ia") and 25 <= edad <= 50:
        contador_iot_ia_masculino_25_50 += 1

    # Métrica 2: Porcentaje de empleados no femeninos, entre 33 y 40 años, que NO votaron por IA
    if genero != "femenino" and 33 <= edad <= 40:
        contador_total_no_femenino_33_40 += 1
        if tecnologia != "ia":
            contador_no_ia_no_femenino_33_40 += 1

    # Métrica 3: Empleado masculino de mayor edad
    if genero == "masculino" and edad > edad_max_masculino:
        edad_max_masculino = edad
        nombre_max_masculino = nombre
        tecnologia_max_masculino = tecnologia

    contador = contador + 1

# Calcular porcentaje para métrica 2
porcentaje_no_ia = 0
if contador_total_no_femenino_33_40 > 0:
    porcentaje_no_ia = (contador_no_ia_no_femenino_33_40 / contador_total_no_femenino_33_40) * 100

# Mostrar resultados
print("\nResultados de la encuesta:")
print("1. Cantidad de empleados masculinos que votaron por IOT o IA (25-50 años):", contador_iot_ia_masculino_25_50)
print("2. Porcentaje de empleados no femeninos (33-40 años) que NO votaron por IA:", porcentaje_no_ia, "%")
print("3. Empleado masculino de mayor edad:")
print("   Nombre:", nombre_max_masculino)
print("   Tecnología elegida:", tecnologia_max_masculino)