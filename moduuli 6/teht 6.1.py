import random
def noppa():
    heitot = random.randint(1,6)
    print(f"Nopansilmäluku oli {heitot}")
    return heitot
while True:
    luku = noppa()
    if luku == 6:
        break
