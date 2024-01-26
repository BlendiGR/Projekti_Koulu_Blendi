
kuhan_pituus = float(input("Kerro kuhan pituus centtimetreinä: "))

def kuhan_mittaaja(kuhan_pituus):
    if kuhan_pituus < 37:
        jäljellä_oleva = 37 - kuhan_pituus
        print(f"Kuha on alamittainen. Laske takaisin järveen. Puuttuu {jäljellä_oleva} centtimetriä pyyntimitasta.")

kuhan_mittaaja(kuhan_pituus)
