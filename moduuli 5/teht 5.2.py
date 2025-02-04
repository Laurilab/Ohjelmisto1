lukujono = []
luku = input("Anna lukuja, tyhjä vastaus lopettaa ohjelman: ")
while luku != "":
    luku = int(luku)

    lukujono.append(luku)
    lukujono.sort()
    luku = (input("Anna lukuja, tyhjä vastaus lopettaa ohjelman: "))
else:
    lukujono.sort(reverse=True)
    print(lukujono[:5])

