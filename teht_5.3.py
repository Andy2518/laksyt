luku = int(input("Syötä luku:"))

if luku <= 1:
    print("Ei ole alkuluku.")
else:
    for luvut in range(2, luku):
        if luku % luvut == 0:
            print("Ei ole alkuluku.")
            break
    else:
        if luku > 1:
            print("On alkuluku.")

