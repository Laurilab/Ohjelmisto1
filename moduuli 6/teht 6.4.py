def lukusumma(summa):
    vastaus = sum(summa)
    print(f"lukujonon summa on: {vastaus}")
    return


luvut = [float(input("Anna luku lopuksi ohjelma summaa luvut yhteen: ")) for _ in range(4)]
tulos = lukusumma(luvut)


