oikea_tunnus = "python"
oikea_salasana = "rules"

while True:
    ktunnuksen_syotto = input("Anna tunnus:")
    salasanan_syotto = input("Anna salasana:")

    if ktunnuksen_syotto != oikea_tunnus or salasanan_syotto != oikea_salasana:
        print("Käyttätunnus tai salasana ei ole oikea.")
        print("Pääsy evästetty.")
    else:
        print("Tervetuloa!")
        break

