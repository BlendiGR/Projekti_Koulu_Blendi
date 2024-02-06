import mariadb
import sys
from geopy import distance

try:
    conn = mariadb.connect(
        user = "root",
        password = "root",
        host = "localhost",
        database = "lentopeli"
    )
except mariadb.Error as error:
    print(f"Virhe tapahtunut : {error}")

kursori = conn.cursor()

inputti1 = input("Anna ICAO : ")
inputti2 = input("Anna toinen ICAO : ")

kursori.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = ? OR ident = ?", (inputti1, inputti2,))

vastaukset = kursori.fetchall()
kursori.close()
if not vastaukset:
    print("Virhe haussa. Yritä uudelleen sijoittamalla oikeat ICAO koodit.")
else:
    lentokenttä1 = vastaukset[0]
    lentokenttä2 = vastaukset[1]
    matka = distance.distance(lentokenttä1, lentokenttä2).km
    print(f"Lentokenttien välinen matka on {round(matka)} kilometriä.")