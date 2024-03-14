def adivinar_numero():
    from random import randint
    numero = randint(1,10)
    intento = input("Adivina el número: ")
    if numero == intento:
        print("Has acertado!!!")
    elif numero != intento:
        print("No has acertado :(")
    pass