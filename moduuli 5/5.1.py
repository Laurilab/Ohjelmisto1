import random

nopat = int(input("Kerro noppien lukumäärä:\n"))
summa = [random.randint(1, 6) for _ in range(nopat)]
print(f"Noppien silmäluvut:\n{summa}")
print(f" Noppien silmälukujen summa on:\n{sum(summa)}")

