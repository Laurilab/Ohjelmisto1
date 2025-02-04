def lukusumma(summa):
    vastaus = [numero for numero in summa if numero % 2 == 0]
    print(f"lukujonon summa on: {vastaus}")
    return


luvut = [float(input("Anna luku lopuksi ohjelma poistaa parittomat listasta: ")) for _ in range(4)]
tulos = lukusumma(luvut)