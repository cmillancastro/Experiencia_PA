def adivinar_numero():
    from random import randint
    numero = randint(1,10)
    intento = input("Adivina el número (elige entre el 1 y el 10): ")
    if numero == intento:
        print("Has acertado!!!")
    elif numero != intento:
        strnumero = str(numero)
        string = "No has acertado :(, el número era " + str(numero)
        print(string)
    pass