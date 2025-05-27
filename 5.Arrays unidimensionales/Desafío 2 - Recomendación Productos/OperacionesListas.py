def _esta_en_lista(elemento: str, lista: list) -> bool:
    """
    Función auxiliar para verificar si un elemento ya existe en una lista.
    Recorre la lista comparando elementos.
    """
    esta = False
    for i in range(len(lista)):
        if lista[i] == elemento:
            esta = True
            break
    return esta

def encontrar_productos_comunes(lista_a: list, lista_b: list) -> list:
    """
    Encuentra los productos que están en ambas listas (intersección).
    Devuelve una lista de productos comunes sin duplicados.
    """
    comunes = []
    for i in range(len(lista_a)):
        producto_a = lista_a[i]
        # Verificamos si el producto_a está en lista_b
        if _esta_en_lista(producto_a, lista_b):
            # Si está en ambas, verificamos que no lo hayamos agregado ya a comunes
            if not _esta_en_lista(producto_a, comunes):
                comunes += [producto_a]
    return comunes

def encontrar_productos_exclusivos(lista_principal: list, lista_comparar: list) -> list:
    """
    Encuentra los productos que están en la lista_principal pero NO en lista_comparar.
    Devuelve una lista de productos exclusivos sin duplicados. (Diferencia A - B)
    """
    exclusivos = []
    for i in range(len(lista_principal)):
        producto = lista_principal[i]
        # Verificamos si el producto NO está en lista_comparar
        if not _esta_en_lista(producto, lista_comparar):
            # Si no está en la otra lista, verificamos que no sea un duplicado en nuestra lista de exclusivos
            if not _esta_en_lista(producto, exclusivos):
                exclusivos += [producto]
    return exclusivos

def obtener_catalogo_total(lista_a: list, lista_b: list) -> list:
    """
    Crea una lista con todos los productos de ambas listas, sin duplicados (unión).
    """
    catalogo = []
    # Agregamos elementos únicos de la lista_a
    for i in range(len(lista_a)):
        producto = lista_a[i]
        if not _esta_en_lista(producto, catalogo):
            catalogo += [producto]
    
    # Agregamos elementos únicos de la lista_b que no estén ya en el catálogo
    for i in range(len(lista_b)):
        producto = lista_b[i]
        if not _esta_en_lista(producto, catalogo):
            catalogo += [producto]
    return catalogo