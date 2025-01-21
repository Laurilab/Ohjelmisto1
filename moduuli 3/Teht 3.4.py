print("Tervetuloa karkausvuoden tarkastajaan")
vuosiluku = int(input("Kerro vuosiluku:"))
if vuosiluku % 4==0 and vuosiluku % 100!=0 or vuosiluku % 400 == 0:
    print("vuosi on karkausvuosi")
else:
    print("vuosi ei ole karkausvuosi")


