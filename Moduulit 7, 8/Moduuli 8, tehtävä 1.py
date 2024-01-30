
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

cur = conn.cursor()

inputti = input("Anna lentoaseman ICAO: ").upper()

cur.execute("SELECT * FROM airport WHERE ident = ?", (inputti,))

results = cur.fetchall()

if results:
    for row in results:
        print(row[3])
else:
    print("Ei tuloksia löytynyt.")

cur.close()
conn.close()
