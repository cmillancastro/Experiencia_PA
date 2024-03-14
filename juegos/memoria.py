def memoria():
    "Esta función representa el juego de memoria. Debes generar una secuencia de números al azar y mostrarla al usuario. Luego, debes pedir al usuario que repita la secuencia. Se debe mostrar un mensaje si el usuario acierta o no."
    from random import randint
    numero = ""
    for i in range(4):
        digito = randint(0,9)
        numero += str(digito)
    string = "Intenta recordar este número: " + numero
    print(string)
    intento = input("¿Cuál era el número?: ")
    if intento == numero:
        print("Has acertado !!")
    elif intento != numero:
        print("No lo has logrado :(, el número era " + numero)

    pass