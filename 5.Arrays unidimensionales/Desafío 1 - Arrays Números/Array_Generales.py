def mostrar_pyn(datos: list) -> str:
    p = 0
    n = 0
    for i in range(len(datos)):
        if datos[i] > 0:
            p += 1
        elif datos[i] < 0:
            n += 1
    return f"\n📊 Se ingresaron {p} números positivos y {n} negativos."

def sumar_pares(datos: list) -> int:
    pares = 0
    for i in range(len(datos)):
        if datos[i] % 2 == 0:
            pares += datos[i]
    return pares

def encontrar_max_imp(datos: list) -> int:
    impares = []
    for i in range(len(datos)):
        if datos[i] % 2 != 0:
            impares += [datos[i]]
    maximo = 0       
    for j in range(len(impares)):
        if impares[j] > maximo:
            maximo = impares[j]
    return maximo

def mostrar_ordenados(datos: list) -> str:  
    resultado = ""
    for i in range(len(datos)):
        resultado += f"🔢 Ingreso {i+1}: {datos[i]}\n"
    return resultado

def listar_pares(datos: list) -> list:
    lista_pares = []
    for i in range(len(datos)):
        if datos[i] % 2 == 0:
            lista_pares += [datos[i]]
    return lista_pares

def mostrar_pos_imp(datos: list) -> list:
    dato_imp = []
    for i in range(len(datos)):
        if i % 2 != 0:
            dato_imp += [datos[i]]   
    return dato_imp
