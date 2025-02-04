import random
def noppa(sivut):
    heitot = random.randint(1,sivut)
    print(f"Nopansilmäluku oli {heitot}")
    return heitot
n = 0
tahkot = int(input("Anna tahkojen lukumäärä:"))
while True:
    luku = noppa(tahkot)
    print(n)
    n += 1
    if luku == tahkot :
        break