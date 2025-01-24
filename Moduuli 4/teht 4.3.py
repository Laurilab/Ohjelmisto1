

number1 = input("Anna luku: ")
suurin = None
pienin = None
while number1 != "":

    print(number1)
    if suurin is None and pienin is None:
        suurin = float(number1)
        pienin = float(number1)
    else:
        number1 = float(number1)
        if number1 > suurin:
            suurin = number1
        if number1 < pienin:
            pienin = number1
    number1 = input("Anna luku: ")
else:
    print(f"pienin luku on {pienin}, ja suurin luku on {suurin}")










