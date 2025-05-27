from OperacionesListas import encontrar_productos_exclusivos

def generar_recomendaciones_para_usuario(nombre_usuario: str, compras_usuario: list, compras_otro_usuario: list) -> list:
    """
    Genera recomendaciones para un usuario basándose en lo que el otro usuario compró
    y el usuario actual no.
    """
    # Productos que el otro usuario compró y el usuario actual no
    recomendaciones = encontrar_productos_exclusivos(compras_otro_usuario, compras_usuario)
    return recomendaciones