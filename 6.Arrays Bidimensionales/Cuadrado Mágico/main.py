from InputMatriz import ingresar_dimension_matriz, ingresar_matriz_manual
from ValidacionesMatriz import verificar_rango_y_unicidad_completa
from OperacionesMatriz import (
    calcular_constante_magica,
    sumar_fila,
    sumar_columna,
    sumar_diagonal_principal,
    sumar_diagonal_secundaria,
    mostrar_matriz_formato
)

def verificar_si_es_cuadrado_magico(matriz: list, n: int) -> bool:
    """
    Verifica todas las condiciones para determinar si la matriz es un cuadrado mágico.
    """
    es_magico_final = True # Variable de resultado
    
    if not verificar_rango_y_unicidad_completa(matriz, n):
        print("Resultado: No es un cuadrado mágico (los números no van de 1 a n*n o hay repetidos/faltantes).")
        es_magico_final = False
    
    # Solo continuamos con las sumas si la validación anterior pasó
    if es_magico_final:
        constante_m = calcular_constante_magica(n)
        print(f"\nConstante mágica esperada (M): {constante_m}")

        print("Suma de filas:")
        for i in range(n):
            if not es_magico_final: break # Si ya falló, no seguir
            suma_f = sumar_fila(matriz, i)
            print(f"  Fila {i+1}: {suma_f}")
            if suma_f != constante_m:
                print("Resultado: No es un cuadrado mágico (falla suma de fila).")
                es_magico_final = False
        
        if es_magico_final: # Solo seguir si las filas estuvieron bien
            print("Suma de columnas:")
            for j in range(n):
                if not es_magico_final: break
                suma_c = sumar_columna(matriz, j, n)
                print(f"  Columna {j+1}: {suma_c}")
                if suma_c != constante_m:
                    print("Resultado: No es un cuadrado mágico (falla suma de columna).")
                    es_magico_final = False

        if es_magico_final: # Solo seguir si filas y columnas estuvieron bien
            suma_dp = sumar_diagonal_principal(matriz, n)
            print(f"Suma Diagonal Principal: {suma_dp}")
            if suma_dp != constante_m:
                print("Resultado: No es un cuadrado mágico (falla suma diagonal principal).")
                es_magico_final = False

        if es_magico_final: # Solo seguir si todo lo anterior estuvo bien
            suma_ds = sumar_diagonal_secundaria(matriz, n)
            print(f"Suma Diagonal Secundaria: {suma_ds}")
            if suma_ds != constante_m:
                print("Resultado: No es un cuadrado mágico (falla suma diagonal secundaria).")
                es_magico_final = False
                
    return es_magico_final 

def main() -> None:
    print("🌟 Verificador de Cuadrados Mágicos 🌟")
    
    orden_n = ingresar_dimension_matriz()
    matriz_usuario = ingresar_matriz_manual(orden_n)
    
    mostrar_matriz_formato(matriz_usuario, orden_n)
    
    es_magico = verificar_si_es_cuadrado_magico(matriz_usuario, orden_n)
    
    if es_magico:
        print("\n🎉 ¡La matriz es un CUADRADO MÁGICO! 🎉")
    else:
        # El mensaje específico del fallo ya se imprimió dentro de verificar_si_es_cuadrado_magico
        # o en verificar_rango_y_unicidad_completa
        print("\n😕 La matriz NO es un cuadrado mágico.")
    
    return None 

if __name__ == "__main__":
    main()