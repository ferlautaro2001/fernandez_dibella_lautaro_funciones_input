
secuencia_externa = [1,2,3,4,5]
secuencia_interna = [1,2,3,4,5]

for i in secuencia_externa:
            # Código del bucle externo (se ejecuta una vez por cada elemento externo)
            print(f"Iteración Externa: {i}")

            for j in secuencia_interna:
                # Código del bucle interno (se ejecuta completamente por cada iteración externa)
                print(f"  Iteración Interna: {j} (dentro de Externa {j})")
            print("-" * 10) # Separador para claridad