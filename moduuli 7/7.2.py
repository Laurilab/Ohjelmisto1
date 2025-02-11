joukko = set()
while True:
    nimet = input("Syötä nimi, tyhjä merkki ohjelma lopettaa jonon:")
    if nimet == "":
        break
    if nimet in joukko:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        joukko.add(nimet)
for nimet in joukko:
    print(nimet)
