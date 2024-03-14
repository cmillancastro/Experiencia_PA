def cachipun():
    from random import randint
    azar = randint(1,3)
    jugador = input("Elige entre piedra, papel o tijera: ")
    jugador = jugador.lower()
    if azar == 1:
        computadora = "piedra"
    elif azar == 2:
        computadora = "papel"
    elif azar == 3:
        computadora = "tijera"
    if jugador == computadora:
        print("Han empatado! Intentálo de nuevo...")
        return cachipun()
    elif jugador != computadora:
        if jugador == "tijera":
            if computadora == "piedra":
                print("Has perdido contra la piedra :(")
            elif computadora == "papel":
                print("Has ganado contra el papel !!")
        elif jugador == "piedra":
            if computadora == "tijera":
                print("Has ganado contra la tijera !!")
            elif computadora == "papel":
                print("Has perdi1do contra el papel :(")
        elif jugador == "papel":
            if computadora == "tijera":
                print("Has perdido contra la tijera :(")
            elif computadora == "piedra":
                print("Has ganado contra la piedra !!")
    pass