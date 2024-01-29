import math


def pizza_laskuri(halkasija, hinta):
    pizzan_koko = 2 * math.pi * (halkasija / 2)
    pizzanhinta_laadusuhde = pizzan_koko / hinta
    return pizzanhinta_laadusuhde


halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija cm: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija cm: "))
hinta2 = float(input("Anna toisen pizzan hinta euroina: "))

kokohinta1 = pizza_laskuri(halkaisija1, hinta1)
kokohinta2 = pizza_laskuri(halkaisija2, hinta2)

if kokohinta1 < kokohinta2:
    print("Ensimmäinen pizza on paremppi vastine rahalle.")
elif kokohinta1 > kokohinta2:
    print("Toinen pizza on parempi vastine rahalle.")
else:
    print("Molemmat pizzat ovat yhtä kalliita.")
