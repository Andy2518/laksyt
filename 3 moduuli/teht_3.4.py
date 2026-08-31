vuosiluku = int(input("Anna vuosiluku:"))

if vuosiluku % 400 == 0:
    print(f"Tämä on karkausvuosi {vuosiluku}")
elif vuosiluku % 100:
    print(f" Tämä ei ole karkausvuosi {vuosiluku}")
elif vuosiluku % 4:
    print(f"Tämä on karkausvuosi {vuosiluku}")
else:
    print(f"Ei ole karkausvuosi")
