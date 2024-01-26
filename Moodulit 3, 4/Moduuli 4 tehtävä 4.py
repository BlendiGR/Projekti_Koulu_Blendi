import random

randomi_numero = random.randint(1, 10)

while True:
    arvauspeli_numero = int(input("Arvaa numero : "))
    if arvauspeli_numero < randomi_numero:
        print("Numero liian pieni arvaa uudelleen")
    if arvauspeli_numero > randomi_numero:
        print("Numero liian suuri arvaa uudelleen")
    if arvauspeli_numero == randomi_numero:
        print("OIKEIN!")
        break
