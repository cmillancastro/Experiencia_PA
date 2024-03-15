def adivinar_par_o_impar():
    from random import randint
    paridad = input("¿El numero es par o impar?: ")
    paridad = paridad.lower()
    numeroaleatorio = randint(0, 100)
    if numeroaleatorio%2 == 0:
        if paridad == "par":
            print("Has acertado!! El número " + str(numeroaleatorio) + "  es par")
        else:
            print("No has acertado :( " + str(numeroaleatorio) + " no es impar")
    elif numeroaleatorio%2 != 0:
        if paridad == "par":
            print("No has acertado :( " + str(numeroaleatorio) + " no es par")
        else:
            print("Has acertado!! El número " + str(numeroaleatorio) + "  es impar")
    pass

# Hola Cata estoy probando