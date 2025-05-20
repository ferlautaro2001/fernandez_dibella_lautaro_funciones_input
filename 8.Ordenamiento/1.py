# Crear una función llamada ordenar_array que reciba como parámetro un array de números enteros y lo ordene de forma ascendente. La función debe implementar como algoritmo de ordenamiento el método de la burbuja. Además, como parámetro opcional debe recibir un booleano (que por default está en False), que en caso de ser True ordena el vector en forma descendente.

def ordenar_array(matriz: int, desc: False):
    if desc == False:
        for i in range(0, len(matriz)-1, 1):
            for j in range(i+1, len(matriz), 1):
                if matriz[i] > matriz[j]:
                    auxiliar = matriz[i]
                    matriz[i] = matriz[j]
                    matriz[j] = auxiliar
    elif desc == True:
        for i in range(0, len(matriz)-1, 1):
            for j in range(i+1, len(matriz), 1):
                if matriz[i] > matriz[j]:
                    auxiliar = matriz[i]
                    matriz[i] = matriz[j]
                    matriz[j] = auxiliar
    return matriz
