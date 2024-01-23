
käyttätunnukset_ja_salasanat = {"python": "rules"}
kokeilu_kerrat = 0
for i in range(0, 5):
        käyttäjätunnus = input("Käyttäjätunnus : ")
        salasana = input("Salasana :  ")
        if käyttäjätunnus in käyttätunnukset_ja_salasanat and käyttätunnukset_ja_salasanat[käyttäjätunnus] == salasana:
            print("Tervetuloa")
            break
        else:
            kokeilu_kerrat += 1
            print(f"Käyttäjätunnukset virheelliset. Yritä uudelleen. {5 - kokeilu_kerrat} kokeilua jäljellä. ")
else:
    print("Kaikki pääsykerrat käytetty. Pääsy evätty.")
