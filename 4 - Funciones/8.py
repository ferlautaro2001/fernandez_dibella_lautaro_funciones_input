# Define una función que encuentre el máximo de tres números. La función debe aceptar tres
# argumentos y devolver el número más grande.

def encontrar_maximo(num1,num2,num3):

    maximo = num1
    if num2>num3:
        competidor = num2
    elif num3>num2:
        competidor = num3
    else:
        pass

    if maximo<competidor:
        maximo = competidor
    
    return maximo 

x = encontrar_maximo(2222,3333,4444)

print(x)