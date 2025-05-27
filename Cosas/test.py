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
