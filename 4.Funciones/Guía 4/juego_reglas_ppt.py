def mostrar_elemento(eleccion: int) -> str:
    """
    Convierte la elección numérica en un texto legible.
    """
    nombre_elemento = ""
    if eleccion == 1:
        nombre_elemento = "Piedra"
    elif eleccion == 2:
        nombre_elemento = "Papel"
    elif eleccion == 3:
        nombre_elemento = "Tijera"
    else:
        nombre_elemento = "Desconocido"
    return nombre_elemento

def verificar_ganador_ronda(jugador: int, maquina: int) -> str:
    """
    Determina quién ganó la ronda según las elecciones.
    Retorna: "Jugador", "Máquina", o "Empate".
    """
    ganador = ""
    if jugador == maquina:
        ganador = "Empate"
    elif (jugador == 1 and maquina == 3) or (jugador == 3 and maquina == 2) or (jugador == 2 and maquina == 1):
        ganador = "Jugador"
    else:
        ganador = "Máquina"
    return ganador

def verificar_estado_partida(aciertos_jugador: int, aciertos_maquina: int, ronda_actual: int) -> bool:
    """
    Determina si la partida sigue en curso o ha finalizado.
    True: la partida sigue. False: la partida ha finalizado.
    La regla de "2 victorias consecutivas" se maneja en la lógica principal.
    """
    sigue_partida = True
    if aciertos_jugador < 2 and aciertos_maquina < 2:
        if ronda_actual <= 3:
            sigue_partida = True
        elif aciertos_jugador == aciertos_maquina: # Después de ronda 3, sigue si hay empate
            sigue_partida = True
        else: # Después de ronda 3, no hay empate, y nadie tiene 2: termina.
            sigue_partida = False
    else: # Alguien ya tiene 2 victorias (o más, si la lógica de fin no actuó antes)
        sigue_partida = False
    return sigue_partida

def verificar_ganador_partida(aciertos_jugador: int, aciertos_maquina: int) -> str:
    """
    Determina quién ganó la partida comparando los aciertos finales.
    """
    ganador_final = ""
    if aciertos_jugador > aciertos_maquina:
        ganador_final = "Jugador"
    elif aciertos_maquina > aciertos_jugador:
        ganador_final = "Máquina"
    else:
        # Este caso no debería darse si el desempate funciona correctamente hasta un ganador.
        ganador_final = "Empate Final (Revisar Lógica de Desempate)"
    return ganador_final