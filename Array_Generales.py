# 1. Ingresar datos: Permitir al usuario ingresar 10 números enteros en el rango de -1000 a 1000.

def ingresar_datos(total_ingresos: int, maximo, minimo):  
    datos = []

    for i in range(total_ingresos):
        while True:
            ingreso = input(f"Ingrese el número {i+1}/10 (debe estar entre {minimo} y {maximo}): ")
            es_valido = True
            if len(ingreso) == 0:
                es_valido = False
            else:
                indice = 0
                if ingreso[0] == '+' or ingreso[0] == '-':
                    if len(ingreso) == 1:
                        es_valido = False  # No puede ser solo el signo
                    else:
                        indice = 1  # Salta el signo en la validación
                while indice < len(ingreso):
                    ascii_val = ord(ingreso[indice])
                    if ascii_val < ord('0') or ascii_val > ord('9'):
                        es_valido = False
                        break
                    indice += 1
            if not es_valido:
                print("Error: Ingrese solo caracteres numéricos válidos (puede comenzar con '+' o '-').")
                continue
            # Convierto a entero y verifico rango.
            numero = int(ingreso)
            if minimo <= numero <= maximo:
                datos += [numero] 
                break
            else:
                print(f"Error: El número ingresado está fuera del rango permitido ({minimo} y {maximo}). Intente de nuevo.")
    return datos

datos = ingresar_datos(10, 1000, -1000)
print("Números ingresados:", datos)

# 2. Cantidad de positivos y negativos: Mostrar cuántos números ingresados son positivos y cuántos son negativos.

def mostrar_pyn(datos: list) -> str :
    p = 0
    n = 0
    for i in range(len(datos)):
        
        if datos[i] > 0:
            p += 1
        elif datos [i] < 0:
            n +=1
    return f"Se ingresaron {p} números positivos y {n} números negativos"

resultado = mostrar_pyn(datos)
print (resultado)

# 3. Suma de los números pares: Calcular y mostrar la sumatoria de los números pares.

def sumar_pares(datos: list) -> int:
    pares = 0
    for i in range (len(datos)):
        if datos[i] % 2 == 0:
            pares += datos[i]
        else:
            pass
    return pares 

pares = sumar_pares(datos)
print(pares)

# 4. Mayor número impar: Identificar y mostrar el mayor número impar ingresado.

def encontrar_max_imp(datos:list) -> int :
    impares = []
    for i in range (len(datos)):
        if datos[i] % 2 != 0:
            impares += [datos[i]]
    maximo = 0       
    for j in range (len(impares)):
        if impares[j] > maximo:
            maximo = impares[j]
    return maximo

max_impar = encontrar_max_imp(datos)
print(max_impar)

# 5. Listar los números ingresados: Mostrar todos los números en el orden en que fueron ingresados.

def mostrar_ordenados(datos: list) -> str:  
    resultado = ""
    for i in range(len(datos)):
        resultado += f"El ingreso número {i+1} fue: {datos[i]}\n"
    return resultado

ordenar = mostrar_ordenados(datos)
print(ordenar)

# 6. Listar los números pares: Mostrar únicamente los números pares de la lista.

def listar_pares(datos: list) -> list:
    lista_pares = []
    for i in range (len(datos)):
        if datos[i] % 2 == 0:
            lista_pares += [datos[i]]
        else:
            pass
    return lista_pares

lista_pares = listar_pares(datos)
print(lista_pares)

# 7. Listar los números en posiciones impares: Mostrar los números que se encuentran en posiciones impares dentro de la lista.

def mostrar_pos_imp(datos: list) -> str:
    dato_imp = []
    for i in range(len(datos)):
        if i % 2 != 0: 
            dato_imp += [datos[i]]   
    return dato_imp 

pos_impar = mostrar_pos_imp(datos)
print(pos_impar)

