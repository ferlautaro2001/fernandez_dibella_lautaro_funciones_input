def _es_caracter_digito(caracter: str) -> bool:
    """
    Verifica si un solo carácter es un dígito del '0' al '9'.
    """
    es_digito = False # Inicializamos la variable de resultado
    if (caracter == '0' or caracter == '1' or caracter == '2' or
        caracter == '3' or caracter == '4' or caracter == '5' or
        caracter == '6' or caracter == '7' or caracter == '8' or
        caracter == '9'):
        es_digito = True
    return es_digito 

def _es_formato_entero_simple(cadena: str) -> bool:
    """
    Verifica si una cadena tiene el formato de un número entero positivo simple.
    No maneja signos, solo dígitos.
    """
    formato_valido = True # Suponemos que es válido inicialmente
    if not cadena:
        formato_valido = False
    else:
        for i in range(len(cadena)):
            if not _es_caracter_digito(cadena[i]):
                formato_valido = False
                break # Salimos del bucle si encontramos un no-dígito
    return formato_valido 

def ingresar_dimension_matriz() -> int:
    """
    Solicita al usuario la dimensión (orden n) de la matriz cuadrada.
    Valida que sea un entero positivo.
    """
    n_resultado = 0 # Variable para el resultado
    valido = False
    while not valido:
        entrada_str = input("Ingrese el orden 'n' de la matriz cuadrada (ej: 3 para 3x3): ")
        if _es_formato_entero_simple(entrada_str):
            n_convertido = int(entrada_str)
            if n_convertido > 0:
                n_resultado = n_convertido
                valido = True # Condición para salir del bucle
            else:
                print("Error: El orden 'n' debe ser un entero positivo.")
        else:
            print("Error: Ingrese un número entero positivo válido para el orden 'n'.")
    return n_resultado 

def ingresar_matriz_manual(n: int) -> list:
    """
    Permite al usuario ingresar manualmente los elementos de una matriz nxn.
    Valida que los números estén en el rango [1, n*n] y que no se repitan.
    """
    matriz_resultado = [] # Variable para el resultado
    numeros_ingresados_para_unicidad = []
    max_valor_permitido = n * n
    
    print(f"\n--- Ingreso de la Matriz {n}x{n} ---")
    print(f"Debe ingresar números enteros entre 1 y {max_valor_permitido}, sin repetir.")

    for i in range(n): 
        fila_actual = []
        print(f"\nFila {i+1}:")
        for j in range(n): 
            valido = False
            numero_celda = 0
            while not valido:
                entrada_str = input(f"  Elemento ({i+1},{j+1}): ")
                if _es_formato_entero_simple(entrada_str):
                    numero_convertido = int(entrada_str)
                    if 1 <= numero_convertido <= max_valor_permitido:
                        esta_repetido = False
                        for k in range(len(numeros_ingresados_para_unicidad)):
                            if numeros_ingresados_para_unicidad[k] == numero_convertido:
                                esta_repetido = True
                                break
                        if not esta_repetido:
                            numero_celda = numero_convertido
                            valido = True
                        else:
                            print(f"Error: El número {numero_convertido} ya fue ingresado. Intente con otro.")
                    else:
                        print(f"Error: El número debe estar entre 1 y {max_valor_permitido}.")
                else:
                    print("Error: Ingrese un número entero positivo válido.")
            
            fila_actual += [numero_celda]
            numeros_ingresados_para_unicidad += [numero_celda]
        matriz_resultado += [fila_actual]
    return matriz_resultado 