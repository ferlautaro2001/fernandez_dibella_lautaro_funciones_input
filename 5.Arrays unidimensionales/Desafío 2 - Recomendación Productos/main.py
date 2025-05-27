from OperacionesListas import (
    encontrar_productos_comunes,
    encontrar_productos_exclusivos,
    obtener_catalogo_total
)
from Recomendaciones import generar_recomendaciones_para_usuario

def mostrar_lista(titulo: str, lista: list) -> None:
    """Función auxiliar para mostrar listas de forma clara."""
    print(f"\n--- {titulo} ---")
    if not lista:
        print(" (Ninguno)")
    else:
        for i in range(len(lista)):
            print(f"- {lista[i]}")

def main():
    print("🛒 Sistema de Recomendación de Productos 🛒")

    # Datos predefinidos (historial de compras)
    historial_usuario_A = ["Manzana", "Leche", "Pan", "Queso", "Manzana", "Jugo"]
    historial_usuario_B = ["Leche", "Huevo", "Pan", "Jamon", "Jugo", "Galletas"]
    
    print("\nHistoriales de Compra:")
    mostrar_lista("Usuario A", historial_usuario_A)
    mostrar_lista("Usuario B", historial_usuario_B)

    # 1️⃣ Productos en común
    comunes = encontrar_productos_comunes(historial_usuario_A, historial_usuario_B)
    mostrar_lista("1️⃣ Productos en Común (ambos usuarios)", comunes)

    # 2️⃣ Productos exclusivos
    exclusivos_A = encontrar_productos_exclusivos(historial_usuario_A, historial_usuario_B)
    mostrar_lista("2️⃣ Productos Exclusivos del Usuario A (que B no compró)", exclusivos_A)
    
    exclusivos_B = encontrar_productos_exclusivos(historial_usuario_B, historial_usuario_A)
    mostrar_lista("2️⃣ Productos Exclusivos del Usuario B (que A no compró)", exclusivos_B)

    # 3️⃣ Catálogo total
    catalogo = obtener_catalogo_total(historial_usuario_A, historial_usuario_B)
    mostrar_lista("3️⃣ Catálogo Total de Productos (Unión)", catalogo)

    # 4️⃣ Recomendaciones
    print("\n--- 4️⃣ Sugerencias de Recomendaciones ---")
    # Recomendar a A lo que B compró y A no
    recomendaciones_para_A = generar_recomendaciones_para_usuario("Usuario A", historial_usuario_A, historial_usuario_B)
    if recomendaciones_para_A:
        print(f"✨ Para Usuario A, podrías interesarte en:")
        for i in range(len(recomendaciones_para_A)):
            print(f"  - {recomendaciones_para_A[i]}")
    else:
        print("No hay nuevas recomendaciones para Usuario A basadas en las compras de Usuario B.")

    # Recomendar a B lo que A compró y B no
    recomendaciones_para_B = generar_recomendaciones_para_usuario("Usuario B", historial_usuario_B, historial_usuario_A)
    if recomendaciones_para_B:
        print(f"✨ Para Usuario B, podrías interesarte en:")
        for i in range(len(recomendaciones_para_B)):
            print(f"  - {recomendaciones_para_B[i]}")
    else:
        print("No hay nuevas recomendaciones para Usuario B basadas en las compras de Usuario A.")
    
    print("\nFin del análisis.")

if __name__ == "__main__":
    main()