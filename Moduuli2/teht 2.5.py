Leiviskä = float(input("Anna leiviskät: "))
Naula = float(input("Anna Naula: "))
Luoti = float(input("Anna Luodit: "))
Summa = Leiviskä * 8.512 + Naula * 0.4256 + Luoti * 0.03133
grammat = Summa % 1 * 1000
print(f"Massa nykymittojen mukaan: {int(Summa)}Kg ja {grammat:10.2f}g")


