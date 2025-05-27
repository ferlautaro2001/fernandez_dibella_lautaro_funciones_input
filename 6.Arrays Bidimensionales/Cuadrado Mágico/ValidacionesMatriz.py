def verificar_rango_y_unicidad_completa(matriz: list, n: int) -> bool:
    """
    Verifica que todos los números de 1 a n*n estén presentes exactamente una vez.
    Asume que la matriz es nxn.
    """
    es_valido = True # Variable para el resultado, suponemos validez inicial
    max_valor = n * n
    
    lista_plana = []
    for i in range(n):
        for j in range(n):
            lista_plana += [matriz[i][j]]

    if len(lista_plana) != max_valor:
        es_valido = False 
    
    if es_valido: # Solo continuamos si la cantidad de elementos es correcta
        esperados = []
        for i in range(1, max_valor + 1):
            esperados += [i]

        for i in range(len(esperados)):
            num_esperado = esperados[i]
            encontrado_en_matriz = False
            contador_apariciones = 0
            for k in range(len(lista_plana)):
                if lista_plana[k] == num_esperado:
                    contador_apariciones += 1
                    # No necesitamos 'encontrado_en_matriz' si usamos contador_apariciones
            
            if contador_apariciones != 1: # Cada número esperado debe aparecer exactamente una vez
                es_valido = False
                break # Si falla una vez, ya no es válido
    
    return es_valido 