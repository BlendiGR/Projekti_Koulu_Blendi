import random

def parametriton_funktio():
    return random.randint(1, 6)

def laskija(max_summa):
    summa = 0
    while summa < max_summa:
        tulos = parametriton_funktio()
        summa += tulos
        print(f"Heitto: {tulos}, Väliaikainen summa: {summa}")
        if summa >= max_summa:
            break

inputti = int(input("Nopan maksimisilmäluku: "))
laskija(inputti)