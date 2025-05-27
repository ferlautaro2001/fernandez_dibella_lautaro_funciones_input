from Especificas import pedir_opcion_menu
from Input import ingresar_datos
from Array_Generales import (
    mostrar_pyn,
    sumar_pares,
    encontrar_max_imp,
    mostrar_ordenados,
    listar_pares,
    mostrar_pos_imp
)

def main():
    datos = []
    activo = True

    while activo:
        print("""
🧮  MENÚ DE OPCIONES:
1️⃣  Ingresar datos
2️⃣  Cantidad de positivos y negativos
3️⃣  Suma de los números pares
4️⃣  Mayor número impar
5️⃣  Listar los números ingresados
6️⃣  Listar los números pares
7️⃣  Listar los números en posiciones impares
8️⃣  Salir
""")
        opcion = pedir_opcion_menu(1, 8)
        match opcion:
            case 1:
                datos = ingresar_datos(10, 1000, -1000)
                print("\n✅ Datos ingresados correctamente.")

            case 2:
                if datos:
                    print(mostrar_pyn(datos))
                else:
                    print("⚠️ Primero debe ingresar los datos (opción 1).")

            case 3:
                if datos:
                    print(f"\n➕ La suma de los números pares es: {sumar_pares(datos)}")
                else:
                    print("⚠️ Primero debe ingresar los datos (opción 1).")

            case 4:
                if datos:
                    print(f"\n🔺 El mayor número impar es: {encontrar_max_imp(datos)}")
                else:
                    print("⚠️ Primero debe ingresar los datos (opción 1).")

            case 5:
                if datos:
                    print("\n" + mostrar_ordenados(datos))
                else:
                    print("⚠️ Primero debe ingresar los datos (opción 1).")

            case 6:
                if datos:
                    print(f"\n🧮 Números pares: {listar_pares(datos)}")
                else:
                    print("⚠️ Primero debe ingresar los datos (opción 1).")

            case 7:
                if datos:
                    print(f"\n📌 Números en posiciones impares: {mostrar_pos_imp(datos)}")
                else:
                    print("⚠️ Primero debe ingresar los datos (opción 1).")

            case 8:
                print("\n👋 Programa finalizado.")
                activo = False

if __name__ == "__main__":
    main()
