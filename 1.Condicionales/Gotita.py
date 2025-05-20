#ENTRADAS
consumo = float(input("Ingrese la cantidad de metros cúbicos consumidos: "))
tipo_cliente = input("Ingrese el tipo de cliente (Residencial, Comercial o Industrial): ").lower().strip()

#PROCESOS
cargo_fijo = 7000
costo_por_m3 = 200
subtotal_consumo = consumo * costo_por_m3
bonificacion = 0
recargo = 0
descuento_especial = 0


match tipo_cliente:
    case "residencial":
        if consumo < 30:
            bonificacion = 0.10 * subtotal_consumo
        elif consumo > 80:
            recargo = 0.15 * subtotal_consumo

    case "comercial":
        if consumo < 50:
            recargo = 0.05 * subtotal_consumo
        elif consumo > 300:
            bonificacion = 0.12 * subtotal_consumo
        elif consumo > 150:
            bonificacion = 0.08 * subtotal_consumo

    case "industrial":
        if consumo < 200:
            recargo = 0.10 * subtotal_consumo
        elif consumo > 1000:
            bonificacion = 0.30 * subtotal_consumo
        elif consumo > 500:
            bonificacion = 0.20 * subtotal_consumo

    case _:
        print("Tipo de cliente no válido.")
        

# Calcular subtotal con bonificaciones/recargos
subtotal_ajustado = cargo_fijo + subtotal_consumo + recargo - bonificacion

# Descuento especial para cliente residencial con factura < $35000
if tipo_cliente == "residencial" and subtotal_ajustado < 35000:
    descuento_especial = 0.05 * subtotal_ajustado
    subtotal_ajustado -= descuento_especial

# Calcular IVA y total
iva = 0.21 * subtotal_ajustado
total = subtotal_ajustado + iva

# SALIDAS
print("\n--- DETALLE DE FACTURA ---")
print(f"Tipo de cliente: {tipo_cliente}")
print(f"Consumo: {consumo} m³")
print(f"Cargo fijo: ${cargo_fijo:.2f}")
print(f"Subtotal por consumo: ${subtotal_consumo:.2f}")
print(f"Bonificación: -${bonificacion:.2f}")
print(f"Recargo: +${recargo:.2f}")
print(f"Descuento especial: -${descuento_especial:.2f}")
print(f"Subtotal ajustado (sin IVA): ${subtotal_ajustado:.2f}")
print(f"IVA (21%): ${iva:.2f}")
print(f"TOTAL A PAGAR: ${total:.2f}")
