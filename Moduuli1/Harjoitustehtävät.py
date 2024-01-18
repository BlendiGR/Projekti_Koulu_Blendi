#Muuttujat ja vuorovaikutteiset ohjelmat
import math
import random


nimi = input("Kerro nimesi : ")
def tervehdys_kone(nimi):
    print(f"Terve, {nimi}!")

tervehdys_kone(nimi)

ympyränsäde = float(input("Kerro ympyrän säde centtimetreinä : "))
def laskuri_kone(ympyränsäde):
    vastaus = ((ympyränsäde**2) * math.pi )
    print(f"Ympyrän pinta-ala : {vastaus}cm")

laskuri_kone(ympyränsäde)

kanta = float(input("Kerro suorakulmion kannan pituus : "))
korkeus = float(input("Kerro suorakulmion korkeus : "))

def suorakulmio_laskuri(kanta, korkeus):
    suorakulmionpiiri = ((kanta * 2) + (korkeus * 2) )
    suorakulmionpintaala = (kanta * korkeus)
    print(f"Suorakulmion piiri on : {suorakulmionpiiri} ja pinta-ala on {suorakulmionpintaala}!")

suorakulmio_laskuri(kanta, korkeus)



kokonaisluku1 = int(input("Saisinko kokonaisluvun : "))
kokonaisluku2 = int(input("Saisinko vielä kokonaisluvun : "))
kokonaisluku3 = int(input("Viimeinen vielä : "))

def kokonaisluvulaskuri(kokonaisluku1, kokonaisluku2, kokonaisluku3):
    summa = kokonaisluku1 + kokonaisluku2 + kokonaisluku3
    tulo = kokonaisluku1 * kokonaisluku2 * kokonaisluku3
    keskiarvo = (kokonaisluku1 + kokonaisluku2 + kokonaisluku3) / 3
    print(f"Lukujen summa on {summa}, tulo on {tulo} ja keskiarvo on {keskiarvo}.")

kokonaisluvulaskuri(kokonaisluku1, kokonaisluku2,kokonaisluku3)

#TEHTÄVÄ 5:

paino1 = float(input("Anna painosi levisköinä : "))
paino2 = float(input("Anna painosi nauloina : "))
paino3 = float(input("Anna painosi luooteina : "))

def painonlaskuri(paino1, paino2, paino3):

    muunnettupainoluoteina = (paino1 * 20 + paino2) * 32
    muunettupainogrammoina = (muunnettupainoluoteina + paino3) * 13.3

    kilogrammat  = muunettupainogrammoina / 1000
    grammat = muunettupainogrammoina % 1000

    return kilogrammat, grammat

kilogrammat, grammat = painonlaskuri(paino1, paino2, paino3)
print(f"Painosi nykymittojen mukaan on {int(kilogrammat)}kg ja {int(grammat)} grammaa!")

#TEHTÄVÄ 6----------------------

def kolminumeroinenlaskuri():
    ykkönen = random.randint(0, 9)
    kakkonen = random.randint(0, 9)
    kolmonen = random.randint(0, 9)
    print(f"{ykkönen}{kakkonen}{kolmonen}")

kolminumeroinenlaskuri()
def nelinumeroinenlaskuri():
    ykkönen = random.randint(1, 6)
    kakkonen = random.randint(1, 6)
    kolmonen = random.randint(1, 6)
    nelonen = random.randint(1, 6)
    print(f"{ykkönen}{kakkonen}{kolmonen}{nelonen}")

nelinumeroinenlaskuri()