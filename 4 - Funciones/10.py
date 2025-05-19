# Crear una función que reciba un número y retorne True si el número es primo, False en caso
# contrario.

def verificador_primo(numero:float)->float:

    divisor = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisor += 1  

    if divisor == 2:
        primo = True
    else:
        primo = False

    return primo

x = verificador_primo(7)

print(x)