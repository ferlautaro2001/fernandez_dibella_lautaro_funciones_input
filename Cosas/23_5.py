# Una reconocida aplicación que opera en la bolsa, desea registrar las inversiones realizadas
# por un grupo VIP de 15 usuarios. Cada usuario puede comprar acciones entre tres
# empresas distintas. Los precios de las acciones están expresados en dólares (hardcodear
# todos los datos)
# Se necesita conocer las siguientes métricas:
# a. Cantidad total de acciones adquiridas por cada usuario.
# b. Promedio de acciones adquiridas por cada empresa entre todos los usuarios.
# c. Usuarios ordenados alfabéticamente de la Z-A junto con el total invertido en las
# distintas empresas.
# d. Total de dinero invertido en la app por todos los usuarios.

# --- ESTRUCTURA DE DATOS (Datos Hardcodeados) ---

# Lista con los nombres de las 3 empresas.

nombres_empresas = ["Meta Platforms", "NVIDIA Corporation", "Amazon.com Inc"]

# Lista con los precios por acción de cada empresa, en el mismo orden.

precios_acciones = [475, 880, 175] 

# Matriz (lista de listas) con los datos de los 15 usuarios.

# Formato de cada lista interna: [Nombre del usuario, Acciones Meta, Acciones NVIDIA, Acciones Amazon]

# Discernir tipos de datos. (2 listas, 1 matriz nombres y otra numérica.)
inversiones_usuarios = [
["Juan Garcia", 10, 5, 12],
["Maria Rodriguez", 5, 15, 8],
["Carlos Martinez", 20, 2, 5],
["Ana Lopez", 12, 8, 20],
["Luis Hernandez", 8, 10, 15],
["Sofia Gonzalez", 15, 12, 3],
["Javier Torres", 2, 20, 10],
["Laura Diaz", 7, 7, 7],
["David Romero", 18, 4, 9],
["Elena Moreno", 4, 18, 14],
["Pablo Alvarez", 9, 9, 18],
["Lucia Jimenez", 11, 6, 11],
["Adrian Navarro", 14, 3, 6],
["Raquel Ruiz", 6, 14, 13],
["Victor Sanchez", 13, 11, 4]
]

# --- a. Cálculo de acciones totales por usuario ---

print("-----------------------------------------")
print("a) Cantidad total de acciones por usuario:")
print("-----------------------------------------")

# Recorremos la matriz de usuarios con un bucle for.

for i in range(len(inversiones_usuarios)):
	# Obtenemos el nombre del usuario (posición 0 de la lista interna)
	nombre_usuario = inversiones_usuarios[i][0]
	acciones_meta = inversiones_usuarios[i][1]
	acciones_nvidia = inversiones_usuarios[i][2]
	acciones_amazon = inversiones_usuarios[i][3]
	total_acciones_usuario = acciones_meta + acciones_nvidia + acciones_amazon
	print(f"- {nombre_usuario}: {total_acciones_usuario} acciones en total.")

# --- b. Promedio de acciones por empresa ---

# Crear lista totales, con diferentes listas para poder recorrer por posiciones.))
print("-----------------------------------------")
print("b) Promedio de acciones por empresa:")
print("------------------------------------")

# Inicializamos los acumuladores para cada empresa en 0

total_acciones_meta = 0
total_acciones_nvidia = 0
total_acciones_amazon = 0

cantidad_de_usuarios = len(inversiones_usuarios)

# Recorremos la matriz de usuarios y sumamos las acciones de cada empresa

# Aca iterariamos la lista totales por posición.))
for i in range(cantidad_de_usuarios):
	total_acciones_meta += inversiones_usuarios[i][1]
	total_acciones_nvidia += inversiones_usuarios[i][2]
	total_acciones_amazon += inversiones_usuarios[i][3]

# Calculamos el promedio dividiendo el total por la cantidad de usuarios

promedio_meta = total_acciones_meta / cantidad_de_usuarios
promedio_nvidia = total_acciones_nvidia / cantidad_de_usuarios
promedio_amazon = total_acciones_amazon / cantidad_de_usuarios

# Mostramos los resultados

print(f"- Promedio de acciones de {nombres_empresas[0]}: {promedio_meta} por usuario.")
print(f"- Promedio de acciones de {nombres_empresas[1]}: {promedio_nvidia} por usuario.")
print(f"- Promedio de acciones de {nombres_empresas[2]}: {promedio_amazon} por usuario.")

# --- c. Listado de usuarios ordenados Z-A con su inversión total ---
#-----------------------------------------------------------------------

print("-----------------------------------------")
print("c) Inversión por usuario (ordenado Z-A):")
print("-----------------------------------------")

# 1. Creamos una nueva lista para almacenar [nombre, inversion_total] para poder ordenarla

lista_inversiones_para_ordenar = []

for i in range(len(inversiones_usuarios)):
    nombre_usuario = inversiones_usuarios[i][0]
    acciones_meta = inversiones_usuarios[i][1]
    acciones_nvidia = inversiones_usuarios[i][2]
    acciones_amazon = inversiones_usuarios[i][3]
    
    # Calculamos la inversión total para este usuario
    inversion_total_usuario = (acciones_meta * precios_acciones[0]) + (acciones_nvidia * precios_acciones[1]) + (acciones_amazon * precios_acciones[2])      
    # Agregamos una nueva lista con el nombre y su inversión a nuestra lista para ordenar
    lista_inversiones_para_ordenar += [[nombre_usuario, inversion_total_usuario]]

# 2. Ordenamos 'lista_inversiones_para_ordenar' con el método de la burbuja.

for i in range(len(lista_inversiones_para_ordenar)):
    for j in range(0, len(lista_inversiones_para_ordenar) - i - 1):
        # Comparamos el nombre del elemento actual con el del siguiente para ordenar de A a Z
        if lista_inversiones_para_ordenar[j][0] > lista_inversiones_para_ordenar[j + 1][0]:
            # Intercambiamos las posiciones de los elementos completos (sublistas)
            auxiliar = lista_inversiones_para_ordenar[j]
            lista_inversiones_para_ordenar[j] = lista_inversiones_para_ordenar[j + 1]
            lista_inversiones_para_ordenar[j + 1] = auxiliar

# 3. Mostramos la lista ya ordenada

for i in range(len(lista_inversiones_para_ordenar)):
    nombre_ordenado = lista_inversiones_para_ordenar[i][0]
    inversion_ordenada = lista_inversiones_para_ordenar[i][1]
    print(f"- {nombre_ordenado}: Total invertido ${inversion_ordenada}")

print("---------------------------------------")
# --- d. Total de dinero invertido en la aplicación ---

#-----------------------------------------------------------------------
print("d) Total de dinero invertido en la app:")
print("---------------------------------------")

# Para ser eficientes, usamos la lista que ya creamos en el punto 'c',
# que contiene las inversiones individuales.
acumulador_total_app = 0
for i in range(len(lista_inversiones_para_ordenar)):
    inversion_usuario = lista_inversiones_para_ordenar[i][1]
    acumulador_total_app = acumulador_total_app + inversion_usuario

print(f"El total de dinero invertido por los 15 usuarios es: ${acumulador_total_app}")
print("---------------------------------------")


