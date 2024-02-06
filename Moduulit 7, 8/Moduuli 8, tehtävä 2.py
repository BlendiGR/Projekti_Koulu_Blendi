
import mariadb
import sys


try:
    conn = mariadb.connect(
        user="root",
        password="root",
        host="127.0.0.1",
        port=3306,
        database="lentopeli"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

inputti = input("Kerro maatunnus : ").upper()
cursor = conn.cursor()

cursor.execute("SELECT type, COUNT(*) FROM airport WHERE iso_country = ? GROUP BY type ", (inputti,))

maatunnustulokset = cursor.fetchall()
cursor.close()

if not maatunnustulokset:
    print("Ei tuloksia")
else:
    for tyyppi, määrä in maatunnustulokset:
        print(f"{tyyppi.title()} : {määrä}")