import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='tietokone020',
         autocommit=True,
         use_pure=True
         )

kursori = yhteys.cursor()

ICAO_1 = input("Anna ICAO_1-koodi: ")
sql1 = f"select latitude_deg, longitude_deg from airport where ident = '{ICAO_1}'"
kursori.execute(sql1)
tulos1 = kursori.fetchone()

ICAO_2 = input("Anna ICAO_2-koodi: ")
sql2 = f"select latitude_deg, longitude_deg from airport where ident = '{ICAO_2}'"
kursori.execute(sql2)
tulos2 = kursori.fetchone()

if tulos1 and tulos2:
    etaisyys = geodesic(tulos1, tulos2).km
    print(f"{ICAO_1} ja {ICAO_2} välinen etäisyys on {etaisyys:.1f} km.")
else:
    print("Jompikumpi tai molemmat ICAO-koodeista ei ole olemassa.")

