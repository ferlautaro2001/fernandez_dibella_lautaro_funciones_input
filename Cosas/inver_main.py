# Importamos las funciones específicas desde el módulo 'libreria'
# (Concepto visto en "9. Módulos y paquetes.pdf", página 6)
from libreria import calcular_acciones_por_usuario, calcular_promedio_por_empresa, informar_inversion_por_usuario_ordenado, calcular_total_inversion_app

# --- Datos Hardcodeados ---
# (Estos datos permanecen en el archivo principal o podrían cargarse de otra fuente)

# Lista de 15 usuarios VIP
usuarios = [
    "Catalina", "Mateo", "Valentina", "Thiago", "Isabella",
    "Bautista", "Martina", "Benjamin", "Sofia", "Lorenzo",
    "Emma", "Joaquin", "Lucia", "Santino", "Olivia"
]

# Lista de 3 empresas disponibles para invertir
empresas = ["Google", "Tesla", "Nvidia"]

# Lista con los precios por acción de cada empresa (en el mismo orden que la lista de empresas)
precios_acciones = [178, 184, 924]

# Matriz de 15x3 (usuarios x empresas) que representa la cantidad de acciones
# que cada usuario compró de cada empresa.
inversiones = [
    [10, 5, 2],    # Catalina
    [3, 8, 12],   # Mateo
    [15, 0, 5],   # Valentina
    [7, 12, 1],   # Thiago
    [2, 9, 9],    # Isabella
    [20, 3, 0],   # Bautista
    [5, 5, 5],    # Martina
    [1, 1, 15],   # Benjamin
    [18, 7, 3],   # Sofia
    [4, 11, 8],   # Lorenzo
    [9, 2, 6],    # Emma
    [0, 20, 10],  # Joaquin
    [12, 6, 4],   # Lucia
    [6, 14, 7],   # Santino
    [11, 4, 11]   # Olivia
]

# --- Programa Principal ---

def main() -> None:
    """
    Función principal que ejecuta todas las operaciones solicitadas.
    """
    # a. Cantidad de acciones por usuario
    # Llama a la función importada pasándole los datos necesarios
    calcular_acciones_por_usuario(usuarios, inversiones)
    
    # b. Promedio de acciones por empresa
    calcular_promedio_por_empresa(empresas, inversiones)
    
    # c. Usuarios ordenados con su total invertido
    # Se pasa la lista 'empresas' como argumento adicional
    informar_inversion_por_usuario_ordenado(usuarios, empresas, inversiones, precios_acciones)
    
    # d. Total de dinero invertido en la app
    total_app = calcular_total_inversion_app(inversiones, precios_acciones)
    print("\n--- d. Total de dinero invertido en la app ---")
    print(f"El total de dinero invertido por todos los usuarios es: ${total_app} dólares.")

# Llamada a la función principal para iniciar el programa
# Esto asegura que main() solo se ejecute cuando este archivo es el script principal.
if __name__ == "__main__":
    main()
