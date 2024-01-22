
#VALINTA RAKENNE IF -----------------------------------------------------------------------------------------------------------------------------------------------------------

#TEHTÄVÄ 1

kuhan_pituus = float(input("Kerro kuhan pituus centtimetreinä: "))

def kuhan_mittaaja(kuhan_pituus):
    if kuhan_pituus < 37:
        jäljellä_oleva = 37 - kuhan_pituus
        print(f"Kuha on alamittainen. Laske takaisin järveen. Puuttuu {jäljellä_oleva} centtimetriä pyyntimitasta.")

kuhan_mittaaja(kuhan_pituus)

#TEHTÄVÄ 2

laiva_hytti = input("Kirjoita laivan hyttiluokka : ").upper()

def laiva_hytti_tarkastaja(laiva_hytti):
    if laiva_hytti == "LUX":
        print("LUX on parvekkeellinen hytti yläkannella.")
    elif laiva_hytti == "A":
        print("A on ikkunallinen hytti autokannen yläpuolella.")
    elif laiva_hytti == "B":
        print("B on ikkunaton hytti autokannen yläpuolella.")
    elif laiva_hytti == "C":
        print("C on ikkunaton hytti autokannen yläpuolella.")
    else:
        print("Virheellinen hyttiluokka!")

laiva_hytti_tarkastaja(laiva_hytti)

#TEHTÄVÄ 3

sukupuoli = input("Mikä on sukupuolesi? (mies/nainen): ").lower()
hemoglobine = float(input("Mikä on hemoglobiini arvosi? (g/l): "))

def hemoglobine_tarkastaja(sukupuoli, hemoglobine):
    if sukupuoli not in ["mies", "nainen"]:
        print("Error. Sukupuolivaihtoehdot ovat vain mies tai nainen!")
    elif sukupuoli == "mies":
        if 134 <= hemoglobine <= 195:
            print("Hemoglobiini arvosi on OK!")
        elif hemoglobine < 134:
            print("Hemoglobiinisi on alhainen.")
        else:  # hemoglobine > 195
            print("Hemoglobiinisi on korkea.")
    elif sukupuoli == "nainen":
        if 117 <= hemoglobine <= 175:
            print("Hemoglobiini arvosi on OK!")
        elif hemoglobine < 117:
            print("Hemoglobiini arvosi on alhainen!")
        else:  # hemoglobine > 175
            print("Hemoglobiini arvosi on korkea.")

hemoglobine_tarkastaja(sukupuoli, hemoglobine)

#TEHTÄVÄ 4

vuosi = int(input("Ilmoita vuosi : "))
def karkausvuosi_laskuri(vuosi):
    if vuosi % 4 == 0 or (vuosi % 100 == 0 and vuosi % 400 == 0):
        print("Vuosi on karkausvuosi")
    else:
        print("Vuosi ei ole karkausvuosi")

karkausvuosi_laskuri(vuosi)

# ALKUEHDOLLINEN TOISTORAKENNE --------------------------------------------------------------------------------------------------------------------------

#TEHTÄVÄ 1

numero = 3
while numero <= 1000:
    print(numero)
    numero += 3

#TEHTÄVÄ 2

tuumakoko = float(input("Anna tuumat : "))
while tuumakoko >= 0:
    print(str(tuumakoko) + "  tuumaa on " + str(tuumakoko * 2.54) + " centtimetriä!")
    tuumakoko = float(input("Anna seuraava tuumakoko (Anna negatiivinen luku lopettaakseen ohjelman) : "))

