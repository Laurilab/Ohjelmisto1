import random
oikealuku = random.randint(1,10 )
luku = float(input("Arvaa luku 1-10: "))
while luku != oikealuku:

    if float(luku) < oikealuku:
        print("Liian pieni arvaus")

    elif float(luku) > oikealuku:
        print("Liian suuri arvaus")
    luku = float(input("Arvaa uudestaan:"))
else:
    print("oikein")