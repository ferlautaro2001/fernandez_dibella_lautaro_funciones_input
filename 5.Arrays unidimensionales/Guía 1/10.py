# Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la unión de los dos arrays.

vector_a = [7, 14, 9, 8, 1]
vector_b = [5, 14, 4, 9, 2]

def encontrar_union(vector_a: list, vector_b: list) -> list:
    union = vector_a
    for i in range(len(vector_b)):
        encontrado = False
        for j in range(len(vector_a)):
            if vector_b[i] == vector_a[j]:
                encontrado = True
                break
        if encontrado == False:
            union += [vector_b[i]]
    return union

union = encontrar_union(vector_a, vector_b)
print(union)  