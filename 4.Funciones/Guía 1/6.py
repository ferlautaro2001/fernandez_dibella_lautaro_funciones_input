# Crea una función que verifique si un número dado es par o impar. La función debe imprimir un
# mensaje indicando si el número es par o impar.


def confirmador(numero:int|float)->str:
    
    if numero % 2 == 0:
        resultado = "Es par"
    else:
        resultado = "Es impar"
    
    return resultado   

print(confirmador(3.5))
