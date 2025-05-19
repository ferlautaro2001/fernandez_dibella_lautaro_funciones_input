# Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.

# Los datos requeridos son:
# Apellido
# Edad, entre 18 y 90 años inclusive.
# Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
# Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

# Una vez ingresados y validados los datos, mostrarlos por pantalla.

apellido = ""
edad = 0
estado_civil = ""
legajo = 0

# Validar apellido
while not apellido:
    apellido = input("Ingrese apellido: ")

# Validar edad
while not 18 <= edad <= 90:
    edad = int(input("Ingrese edad: "))
    if not 18 <= edad <= 90:
        print("Edad inválida. Debe estar entre 18 y 90 años.")

# Validar estado civil
while not (estado_civil == "soltero" or estado_civil == "casado" or estado_civil == "divorciado" or estado_civil == "viudo" or estado_civil == "soltera" or estado_civil == "casada" or estado_civil == "divorciada" or estado_civil == "viuda"):

    estado_civil = input("Ingrese estado civil (Soltero/a, Casado/a, Divorciado/a, Viudo/a): ").lower()

    if not (estado_civil == "soltero" or estado_civil == "casado" or estado_civil == "divorciado" or estado_civil == "viudo" or estado_civil == "soltera" or estado_civil == "casada" or estado_civil == "divorciada" or estado_civil == "viuda"):
        
        print("Estado civil inválido. Debe ser Soltero/a, Casado/a, Divorciado/a o Viudo/a.")

# Validar legajo
while not 1000 <= legajo <= 9999:
    legajo = int(input("Ingrese legajo (4 cifras, sin ceros a la izquierda): "))
    if not 1000 <= legajo <= 9999:
        print("Legajo inválido. Debe ser un valor numérico de 4 cifras sin ceros a la izquierda.")


# Mostrar datos una vez validados
print("Apellido:", apellido, "\nEdad:", edad, "\nEstado civil:", estado_civil, "\nLegajo:", legajo)

