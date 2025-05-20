# Crea una función que verifique si un número dado es par o impar. La función retorna True si el
# número es par, False en caso contrario.

def verificar_paridad(numero:int|float)->bool:

    if numero % 2 == 0:
        bandera_par = True
    elif numero % 2 != 0:
        bandera_par = False

    return bandera_par

chequeo = verificar_paridad(7)

print(chequeo)
