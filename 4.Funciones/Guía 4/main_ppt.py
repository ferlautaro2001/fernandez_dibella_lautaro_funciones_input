# Importar get_int del módulo Input.
from Input import get_int
# Importar las funciones de reglas del juego.
from juego_reglas_ppt import mostrar_elemento, verificar_ganador_ronda, verificar_estado_partida, verificar_ganador_partida

def jugar_piedra_papel_tijera() -> str:
    """
    Gestiona toda la lógica del juego Piedra, Papel o Tijera.
    Retorna "Jugador" o "Máquina" indicando el ganador de la partida.
    """
    aciertos_jugador = 0
    aciertos_maquina = 0
    ronda_actual = 1
    victorias_consecutivas_jugador = 0
    victorias_consecutivas_maquina = 0
    ganador_final_partida = ""

    print("¡Bienvenido a Piedra, Papel o Tijera!")
    print("Reglas: Mejor de 3 rondas. Dos victorias seguidas ganan la partida.")
    print("Si hay empate tras 3 rondas o más y los puntajes están igualados, se juega a desempate.")
    print("----------------------------------------------------")
    print("Elección de la máquina: Cíclica (Piedra, Papel, Tijera, ...).")
    print("----------------------------------------------------")

    while True:
        print(f"\n--- Ronda {ronda_actual} ---")
        print(f"Marcador: Jugador {aciertos_jugador} - Máquina {aciertos_maquina}")
        print(f"Victorias consecutivas: Jugador ({victorias_consecutivas_jugador}), Máquina ({victorias_consecutivas_maquina})")


        # Elección del jugador utilizando get_int del módulo Input
        eleccion_jugador = get_int(
            mensaje="Elige tu jugada (1: Piedra, 2: Papel, 3: Tijera):", # Este mensaje lo imprime get_int
            mensaje_error="Error: Debes ingresar 1, 2 o 3.",
            minimo=1,
            maximo=3,
            reintentos=2 
        )
        # get_int luego usa su propio input("Ingrese el número entero: ")

        if eleccion_jugador == None:
            print("Entrada inválida por el jugador. La máquina gana la partida por abandono.")
            ganador_final_partida = "Máquina"
            break # Termina el bucle while y la partida

        # Elección de la máquina (determinista y cíclica)
        eleccion_maquina = ((ronda_actual - 1) % 3) + 1 
        
        nombre_eleccion_jugador = mostrar_elemento(eleccion_jugador)
        nombre_eleccion_maquina = mostrar_elemento(eleccion_maquina)
        print(f"Jugador eligió: {nombre_eleccion_jugador}")
        print(f"Máquina eligió: {nombre_eleccion_maquina}")

        ganador_ronda = verificar_ganador_ronda(eleccion_jugador, eleccion_maquina)
        
        if ganador_ronda == "Jugador":
            print("🏆 ¡Jugador gana la ronda!")
            aciertos_jugador += 1
            victorias_consecutivas_jugador += 1
            victorias_consecutivas_maquina = 0
        elif ganador_ronda == "Máquina":
            print("🏆 ¡Máquina gana la ronda!")
            aciertos_maquina += 1
            victorias_consecutivas_maquina += 1
            victorias_consecutivas_jugador = 0
        else: 
            print("👔 ¡Empate en esta ronda!")
            victorias_consecutivas_jugador = 0
            victorias_consecutivas_maquina = 0

        # 1. Verificar fin de partida por 2 victorias consecutivas
        if victorias_consecutivas_jugador == 2:
            print("\n¡Jugador gana la partida por 2 victorias consecutivas!")
            ganador_final_partida = "Jugador"
            break 
        if victorias_consecutivas_maquina == 2:
            print("\n¡Máquina gana la partida por 2 victorias consecutivas!")
            ganador_final_partida = "Máquina"
            break

        # 2. Verificar si la partida debe continuar según las reglas de puntaje/rondas
        #    (esto cubre el "mejor de 3" y la continuación en caso de empate post-ronda 3)
        if not verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual):
            ganador_final_partida = verificar_ganador_partida(aciertos_jugador, aciertos_maquina)
            print(f"\n¡Partida terminada! El ganador es: {ganador_final_partida}")
            break
        
        ronda_actual += 1

    return ganador_final_partida

# --- Ejecutar el Juego ---
if __name__ == "__main__":
    ganador_del_juego = jugar_piedra_papel_tijera()
    # El mensaje de ganador ya se imprime dentro de jugar_piedra_papel_tijera
    # cuando la partida termina por una condición que no sea abandono.
    if ganador_del_juego: # Solo si hubo un ganador retornado (no por abandono sin setear)
        print(f"\n🏁🏁🏁 El ganador final del juego es: ¡{ganador_del_juego}! 🏁🏁🏁")