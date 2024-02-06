

lentoasemat = {
    "Helsinki-Vantaan lentoasema": "EFHK",
    "Oulun lentoasema": "EFOU",
    "Rovaniemen lentoasema": "EFRO",
    "Turun lentoasema": "EFTU",
    "Vaasan lentoasema": "EFVA",
    "Kuopion lentoasema": "EFKU",
    "Tampere-Pirkkalan lentoasema": "EFTP",
    "Lappeenrannan lentoasema": "EFLP",
    "Jyväskylän lentoasema": "EFJY",
    "Joensuun lentoasema": "EFJO"
}
vastauksia1 = [
    "ei", "en halua", "en", "ei kiitos", "ei nyt", "ei tarvitse",
    "ei kiinnosta", "en ole kiinnostunut", "ei tällä kertaa", "ei, kiitos",
    "ei tänään", "ehkä myöhemmin", "en nyt", "ei ehkä", "ei todellakaan", "lopettaa", "lopeta"
]

vastauksia2 = [
    "uusi", "laita uusi", "laitan uuden", "lisää uusi", "haluan lisätä",
    "uuden lisäys", "lisään uuden", "uuden lentoaseman", "uusi lisäys", "lisää",
    "haluan lisätä uuden", "uuden tallennus", "uuden syöttö", "tallenna uusi", "kirjaa uusi"
]

vastauksia3 = [
    "nykyinen", "olemassa", "haeolemassa", "olemassaoleva", "onkoolemassa",
    "etsi", "hae", "etsi olemassa oleva", "etsintä", "löydä",
    "etsi nykyinen", "hae tieto", "nykyisen haku", "olemassa olevan etsintä", "löydä nykyinen"
]


def lentoasemahakija():
    while True:
        inputti = input("Haluatko etsiä lentoaseman, syöttää uuden vai lopettaa? : \n").lower().strip()

        if inputti in vastauksia1:
            print("Toiminto lopetettu")
            break

        elif inputti in vastauksia2:
            kysynimi = input("Mikä on lentokentän nimi? : ").title().strip()
            kysyICAO = input("Mikä on lentokentän ICAO koodi? : ").upper().strip()

            if kysynimi and kysyICAO:
                lentoasemat[kysynimi] = kysyICAO
                print(f"Lisätty lentokenttä: {kysynimi} ICAO-koodilla {kysyICAO}")
            else:
                print("Lentokentän nimi tai ICAO koodi puuttuu.")

        elif inputti in vastauksia3:
            kysy_icao = input("Kerro lentokentän ICAO koodi: ").upper()
            loydetty_lentoasema = None

            for lento, icao in lentoasemat.items():
                if icao == kysy_icao:
                    loydetty_lentoasema = lento
                    break

            if loydetty_lentoasema:
                print(f"Löydettiin lentokenttä: {loydetty_lentoasema}")
            else:
                print("Lentokenttää ei löytynyt annetulla ICAO-koodilla.")



lentoasemahakija()
print(lentoasemat)

