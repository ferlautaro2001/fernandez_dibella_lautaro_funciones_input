#  El dueño de una tienda dedicada a la compra/venta de cartas de Yu-Gi-Oh, desea ingresar en el sistema las ventas realizadas en el día de la fecha y a partir de ello, conocer ciertos datos en base a las cartas que se vendieron.

# Deberemos desarrollar un sistema para que el dueño pueda ingresar 20 ventas.

# Nombre de carta
# Precio (número positivo, no puede ser mayor a 200000)
# Tipo (Mágica, monstruo, trampa)
# Rareza (rara, super rara, ultra rara)

# Una vez finalizado el ingreso de datos se desea conocer:

# A. Cantidad de cartas de rareza rara cuyo precio oscile en 50000 y 80000 y sea de tipo Mágica o trampa.
# B. El nombre y tipo de la carta con mayor precio de la rareza super rara.
# C. El porcentaje de rara, super rara y ultra rara hay sobre el total
# D. Determinar el precio promedio por cada tipo de carta
# E. Determinar cuál fue el tipo de carta menos vendida


VENTAS = 20
contador_especial1 = 0
maximo_precio = 0
bandera_primer_super_rara = False
nombre_carta_max_precio = ""
tipo_carta_max_precio = ""

contador_raras = 0
contador_super = 0
contador_ultra = 0

# Para el punto D
acumulador_precio_magica = 0
contador_magica = 0
acumulador_precio_monstruo = 0
contador_monstruo = 0
acumulador_precio_trampa = 0
contador_trampa = 0

for ventas in range(VENTAS):
    # ENTRADAS
    nombre = input("Ingrese el nombre de la carta: ").lower()
    
    precio = int(input("Ingrese el precio: "))
    while precio <= 0 or precio > 200000:
        precio = int(input("Error... Ingrese el precio: "))
    
    tipo = input("Ingrese el tipo (Magica - Monstruo - Trampa): ").lower()
    while tipo != "magica" and tipo != "monstruo" and tipo != "trampa":
        tipo = input("Error... Ingrese el tipo (magica - monstruo - trampa): ")

    rareza = input("Ingrese la rareza (Rara - Super - Ultra): ").lower()
    while rareza != "rara" and rareza != "super" and rareza != "ultra":
        rareza = input("Error... Ingrese la rareza (rara - super - ultra): ")
    
    # PROCESOS
    # A. Cantidad de cartas de rareza rara cuyo precio oscile en 50000 y 80000 y sea de tipo Mágica o trampa.
    if rareza == "rara" and 50000 <= precio <= 80000 and (tipo == "magica" or tipo == "trampa"):
        contador_especial1 += 1
    
    # B. El nombre y tipo de la carta con mayor precio de la rareza super rara.
    if rareza == "super":
        if not bandera_primer_super_rara or precio > maximo_precio:
            maximo_precio = precio
            nombre_carta_max_precio = nombre
            tipo_carta_max_precio = tipo
            bandera_primer_super_rara = True
    
    # C. El porcentaje de rara, super rara y ultra rara hay sobre el total
    if rareza == "rara":
        contador_raras += 1
    elif rareza == "super":
        contador_super += 1
    else:  # ultra
        contador_ultra += 1
    
    # D. Determinar el precio promedio por cada tipo de carta
    if tipo == "magica":
        acumulador_precio_magica += precio
        contador_magica += 1
    elif tipo == "monstruo":
        acumulador_precio_monstruo += precio
        contador_monstruo += 1
    else:  # trampa
        acumulador_precio_trampa += precio
        contador_trampa += 1

# SALIDAS
print("\nRESULTADOS:")
print(f"A. Cantidad de cartas de rareza rara con precio entre 50000 y 80000 de tipo Mágica o trampa: {contador_especial1}")

if bandera_primer_super_rara:
    print(f"B. La carta super rara de mayor precio es: {nombre_carta_max_precio} de tipo {tipo_carta_max_precio}")
else:
    print("B. No se ingresaron cartas de rareza super rara")

# C. Porcentajes de rareza
porcentaje_raras = (contador_raras / VENTAS) * 100
porcentaje_super = (contador_super / VENTAS) * 100
porcentaje_ultra = (contador_ultra / VENTAS) * 100
print(f"C. Porcentajes de rareza:")
print(f"   - rara: {porcentaje_raras:.2f}%")
print(f"   - super rara: {porcentaje_super:.2f}%")
print(f"   - ultra rara: {porcentaje_ultra:.2f}%")

# D. Precio promedio por tipo
print("D. Precio promedio por tipo de carta:")
if contador_magica > 0:
    promedio_magica = acumulador_precio_magica / contador_magica
    print(f"   - Mágica: ${promedio_magica:.2f}")
else:
    print("   - Mágica: No se vendieron")

if contador_monstruo > 0:
    promedio_monstruo = acumulador_precio_monstruo / contador_monstruo
    print(f"   - monstruo: ${promedio_monstruo:.2f}")
else:
    print("   - monstruo: No se vendieron")

if contador_trampa > 0:
    promedio_trampa = acumulador_precio_trampa / contador_trampa
    print(f"   - trampa: ${promedio_trampa:.2f}")
else:
    print("   - trampa: No se vendieron")

# E. Tipo de carta menos vendida
print("E. Tipo de carta menos vendida:")
if contador_magica <= contador_monstruo and contador_magica <= contador_trampa:
    print("   - Mágica")
if contador_monstruo <= contador_magica and contador_monstruo <= contador_trampa:
    print("   - monstruo")
if contador_trampa <= contador_magica and contador_trampa <= contador_monstruo:
    print("   - trampa")