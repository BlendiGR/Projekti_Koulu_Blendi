
numerot = []

while True:
    try:
        käyttäjä_numerot = int(input("Anna numeroita : "))
        numerot.append(käyttäjä_numerot)
    except ValueError:
        break

sortatut_numerot = sorted(numerot)
print(f"Pienin luku on {sortatut_numerot[0]} ja suurin on {sortatut_numerot[-1]}!")
