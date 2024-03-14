def memoria():
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