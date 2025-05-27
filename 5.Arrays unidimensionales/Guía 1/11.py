# Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la diferencia de los dos arrays.

vector_a = [7, 14, 9, 8, 1]
vector_b = [5, 14, 4, 9, 2]

def encontrar_diferencia(vector_a, vector_b):
    diferencia = []
    for i in range(len(vector_a)):
        encontrado = False
        for j in range(len(vector_b)):
            if vector_a[i] == vector_b[j]:
                encontrado = True
                break
        if encontrado == False:
            diferencia += [vector_a[i]]
    return diferencia

diferencia = encontrar_diferencia(vector_a, vector_b)
print(diferencia)  