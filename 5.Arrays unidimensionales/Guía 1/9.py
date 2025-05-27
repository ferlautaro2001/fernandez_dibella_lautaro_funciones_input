# Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la intersección de los dos arrays.

vector_a = [7, 14, 9, 8, 1]
vector_b = [5, 14, 4, 9, 2]

def encontrar_interseccion(vector_a, vector_b):
    interseccion = []
    for i in range(len(vector_a)):
        for j in range(len(vector_b)):
            if vector_a[i] == vector_b[j]:
                interseccion += [vector_a[i]]
                break
    return interseccion 

interseccion = encontrar_interseccion(vector_a, vector_b)
print(interseccion)
