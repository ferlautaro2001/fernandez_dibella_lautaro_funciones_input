# --- Definición de Funciones de la Librería ---

def calcular_acciones_por_usuario(lista_usuarios: list, matriz_inversiones: list) -> None:
    """
    Calcula e imprime la cantidad total de acciones que cada usuario posee.
    Recorre la matriz de inversiones fila por fila (por usuario).

    Args:
        lista_usuarios (list): La lista con los nombres de los usuarios.
        matriz_inversiones (list): La matriz (lista de listas) con las acciones.

    Returns:
        None: La función no retorna valor, imprime el resultado en la terminal.
    """
    print("\n--- a. Cantidad total de acciones por usuario ---")
    # Usamos un bucle for para recorrer las filas (cada fila es un usuario)
    for i in range(len(lista_usuarios)):
        acumulador_acciones = 0
        # Usamos un bucle anidado para recorrer las columnas (cada columna es una empresa)
        for j in range(len(matriz_inversiones[i])):
            # Acumulamos las acciones de cada empresa para el usuario actual
            acumulador_acciones += matriz_inversiones[i][j]
        
        print(f"{lista_usuarios[i]}: {acumulador_acciones} acciones.")

def calcular_promedio_por_empresa(lista_empresas: list, matriz_inversiones: list) -> None:
    """
    Calcula e imprime el promedio de acciones adquiridas por cada empresa.
    Recorre la matriz de inversiones columna por columna (por empresa).

    Args:
        lista_empresas (list): La lista con los nombres de las empresas.
        matriz_inversiones (list): La matriz (lista de listas) con las acciones.

    Returns:
        None: La función no retorna valor, imprime el resultado en la terminal.
    """
    print("\n--- b. Promedio de acciones por empresa ---")
    cantidad_usuarios = len(matriz_inversiones)
    # Recorremos las columnas (empresas)
    for j in range(len(lista_empresas)):
        acumulador_empresa = 0
        # Recorremos las filas (usuarios)
        for i in range(cantidad_usuarios):
            # Acumulamos las acciones para la empresa actual
            acumulador_empresa += matriz_inversiones[i][j]
        
        # Calculamos el promedio
        if cantidad_usuarios > 0: # Evitar división por cero si no hay usuarios
            promedio = acumulador_empresa / cantidad_usuarios
        else:
            promedio = 0
        print(f"Promedio de acciones de {lista_empresas[j]}: {promedio} por usuario.")

def ordenar_listas_descendente(lista_a_ordenar: list, lista_acompanante: list) -> None:
    """
    Ordena una lista de texto de la Z a la A (descendente) usando el método de burbuja.
    Modifica una segunda lista para mantener la correspondencia con la primera.
    
    Args:
        lista_a_ordenar (list): La lista de nombres que se usará como criterio de orden.
        lista_acompanante (list): La lista de valores (ej: totales) que debe ordenarse en paralelo.

    Returns:
        None: La función modifica las listas originales (pasaje por referencia).
    """
    largo_lista = len(lista_a_ordenar)
    # Implementación del algoritmo de ordenamiento de Burbuja
    for i in range(largo_lista):
        for j in range(0, largo_lista - i - 1):
            # Comparamos cadenas de forma lexicográfica para ordenar Z-A
            if lista_a_ordenar[j] < lista_a_ordenar[j+1]:
                # Intercambiamos los nombres de usuario
                aux_usuario = lista_a_ordenar[j]
                lista_a_ordenar[j] = lista_a_ordenar[j+1]
                lista_a_ordenar[j+1] = aux_usuario
                
                # Intercambiamos el total invertido correspondiente
                aux_total = lista_acompanante[j]
                lista_acompanante[j] = lista_acompanante[j+1]
                lista_acompanante[j+1] = aux_total

def informar_inversion_por_usuario_ordenado(lista_usuarios: list, lista_empresas: list, matriz_inversiones: list, precios: list) -> None:
    """
    Calcula el total invertido por cada usuario, los ordena alfabéticamente
    de Z-A e imprime el resultado.

    Args:
        lista_usuarios (list): La lista con los nombres de los usuarios.
        lista_empresas (list): La lista con los nombres de las empresas.
        matriz_inversiones (list): La matriz con las acciones.
        precios (list): La lista con los precios de las acciones.

    Returns:
        None: Imprime el resultado en la terminal.
    """
    print("\n--- c. Usuarios ordenados (Z-A) con su total invertido ---")
    totales_invertidos = []
    # Calculamos el total invertido por cada usuario
    for i in range(len(lista_usuarios)):
        total_dolares_usuario = 0.0
        for j in range(len(lista_empresas)): # Usamos len(lista_empresas) o len(precios)
            # Multiplicamos acciones por precio y acumulamos
            total_dolares_usuario += matriz_inversiones[i][j] * precios[j]
        totales_invertidos += [total_dolares_usuario]

    # Creamos copias para no alterar las listas originales que se pasan como argumento
    # lista_usuarios es la que se va a ordenar, así que su copia es la importante aquí.
    usuarios_copia_ordenar = lista_usuarios[:] 
    
    # Ordenamos las listas (la copia de usuarios y la de totales)
    ordenar_listas_descendente(usuarios_copia_ordenar, totales_invertidos)
    
    # Mostramos los resultados ya ordenados
    for i in range(len(usuarios_copia_ordenar)):
        print(f"{usuarios_copia_ordenar[i]}: invirtió un total de ${totales_invertidos[i]} dólares.")

def calcular_total_inversion_app(matriz_inversiones: list, precios: list) -> float:
    """
    Calcula la suma total de dinero invertido en la aplicación por todos los usuarios.

    Args:
        matriz_inversiones (list): La matriz con las acciones.
        precios (list): La lista con los precios de las acciones.

    Returns:
        float: El monto total de dinero invertido.
    """
    gran_total_invertido = 0.0
    # Recorremos la matriz de inversiones
    for i in range(len(matriz_inversiones)):
        for j in range(len(matriz_inversiones[i])): # Asumiendo que precios tiene la misma cantidad de elementos que columnas en inversiones
            inversion = matriz_inversiones[i][j] * precios[j]
            gran_total_invertido += inversion
    return gran_total_invertido