import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='tietokone020',
         autocommit=True,
         use_pure=True
         )

ICAO = input("Anna ICAO-koodi: ")
sql = f"select name, municipality from airport where ident = '{ICAO}'"
kursori = yhteys.cursor()
kursori.execute(sql)

# Haetaan ja käsitellään tulokset.
tulos = kursori.fetchall()

for rivi in tulos:
    print(rivi)