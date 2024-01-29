import random

def parametriton_funktio():
    return random.randint(1, 6)

def laskija():
    while True:
        tulos = parametriton_funktio()
        print(tulos)
        if tulos == 6:
            break

laskija()