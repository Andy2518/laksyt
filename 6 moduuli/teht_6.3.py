def bensiini(gallona):
    litrat = gallona * 3,785
    return litrat

gallomaara = int(input("Anna gallomäärä:"))

while gallomaara >= 0:
    litramaara = bensiini(gallomaara)
    print(litramaara)
    gallomaara = int(input("Anna gallomäärä:"))

