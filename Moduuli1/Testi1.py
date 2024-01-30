class Car:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämäntekinennopeus = 0
        self.kuljettumatka = 0

    def kiihdytä(self, nopeudenmuutos):
        uusi_nopeus = self.tämäntekinennopeus + nopeudenmuutos
        if 0 <= uusi_nopeus <= self.huippunopeus:
            self.tämäntekinennopeus = uusi_nopeus

    def __str__(self):
        return (f"Rekisteritunnus: {self.rekisteritunnus}, "
                f"Huippunopeus: {self.huippunopeus} km/h, "
                f"Tämänhetkinen nopeus: {self.tämäntekinennopeus} km/h, "
                f"Kuljettu matka: {self.kuljettumatka} km")

# Luodaan auto ja tulostetaan sen tiedot
auto1 = Car("ESH-107", 240)
print(auto1)

# Kiihdytetään autoa ja tulostetaan sen tiedot uudelleen
auto1.kiihdytä(20)
print(auto1)