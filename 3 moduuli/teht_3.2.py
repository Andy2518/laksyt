hyttiluokka = input("Syötä laivan hyttiluokka:")

if hyttiluokka == "LUX":
    print(f"{hyttiluokka} on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print(f"{hyttiluokka} on ikkulallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print(f"{hyttiluokka} on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print(f"{hyttiluokka} on ikkunaton hytti autokannen alapuolella")
else:
    print(f"Virheellinen hyttiluokka.")