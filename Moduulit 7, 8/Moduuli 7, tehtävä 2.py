nimilista = ["Onni", "Rene", "Eemil", "Blendi"]

def nimilista_katsoja(nimilista):
    while True:
        try:
            nimi = input("Kerro nimi :  ").title()
            if nimi == "" or nimi.isdigit():
                print("Syötä oikea nimi")
                break
            elif nimi in nimilista:
                print("Nimi on jo listassa")
            elif nimi not in nimilista:
                nimilista.append(nimi)
                print("Nimi ei ole listassa, nimi lisätty listaan")
            else:
                print("Virhe tapahtunut")
        except ValueError:
            break


nimilista_katsoja(nimilista)
for i in nimilista:
    print(i)


