
vuosi = int(input("Ilmoita vuosi : "))
def karkausvuosi_laskuri(vuosi):
    if vuosi % 4 == 0 or (vuosi % 100 == 0 and vuosi % 400 == 0):
        print("Vuosi on karkausvuosi")
    else:
        print("Vuosi ei ole karkausvuosi")

karkausvuosi_laskuri(vuosi)
