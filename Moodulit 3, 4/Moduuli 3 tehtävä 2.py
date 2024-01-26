
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
