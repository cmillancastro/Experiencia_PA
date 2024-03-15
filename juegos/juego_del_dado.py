def juego_del_dado():
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    import random
    lanzar = input('presiones enter para jugar')
    ptos_jugador = 0
    ptos_com = 0
    while ptos_jugador < 30 and ptos_com < 30:
        input('presione enter para jugar')
        num = random.randint(1,6)
        ptos_jugador += num
        print('jugador posee', ptos_jugador, 'puntos')
        if ptos_jugador < 30:
            num_com = random.randint(1,6)
            ptos_com += num_com
            print('computador posee', ptos_com, 'puntos')
            if ptos_com >= 30:
                print('ha ganado computador')
        else:
            print('ha ganado jugador')

juego_del_dado()


