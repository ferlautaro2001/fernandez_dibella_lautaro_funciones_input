# Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la intersección de los dos arrays. En la foto están los dos arrays. 


vector_a = [4, 6, 9, 8, 7]
vector_b = [5, 6, 4, 7, 2]


def interseccion_sin_in_for(vector_a, vector_b):
    resultado = []
    
    for elemento_a in vector_a:
        # Buscar en vector_b
        encontrado = False
        for elemento_b in vector_b:
            if elemento_a == elemento_b:
                encontrado = True
                break
        
        # Verificar duplicados en resultado
        if encontrado:
            existe = False
            for item in resultado:
                if item == elemento_a:
                    existe = True
                    break
            
            if not existe:
                resultado.append(elemento_a)
    
    return resultado
