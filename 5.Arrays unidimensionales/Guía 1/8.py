# Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
# Una lista de nombres (lista_nombres).
# Un nombre a buscar en la lista (nombre_antiguo).
# Un nombre de reemplazo (nombre_nuevo).
# La función debe realizar las siguientes acciones:
# Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
# Retornar la cantidad total de reemplazos realizados.

lista_nombres = ["Abel", "Caroline", "Dustin", "Aurora", "Abel", "Caroline", "Dustin", "Aurora","Abel", "Caroline", "Dustin", "Aurora"]
nombre_antiguo = "Dustin"
nombre_nuevo = "Kay"


def reemplazar_nombres(lista_nombres: list, nombre_antiguo: str, nombre_nuevo:str ):
    reemplazos = 0
    for i in range (len(lista_nombres)):
        if lista_nombres[i] == nombre_antiguo:
            lista_nombres[i] = nombre_nuevo
            reemplazos += 1
    return reemplazos

reemplazos = reemplazar_nombres(lista_nombres,nombre_antiguo,nombre_nuevo)

print(reemplazos,lista_nombres)