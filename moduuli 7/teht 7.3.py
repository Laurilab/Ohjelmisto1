def uusilento():
    nimi = input("Syötä Lentoaseman nimi:\n")
    icao = input("Syötä lentäaseman ICAO koodi:\n")
    tiedot[icao] = nimi
    return tiedot

def tietohaku():
    icao1 = input("Syötä annetun lentokentän ICAO koodi:")
    if icao1 in tiedot:
        print(tiedot[icao1])
    else:
        print("Annetulla ICAO koodilla ei löytynyt tietoja")





tiedot = {}




while True:

    user_input = input("Syötä a, jos haluat lisätä uuden lentoaseman tiedot,\n"
                "Syötä b, jos haluat hakea jo syötetyn aseman tiedot.\n"
                "Jos haluat lopettaa syötä tyhjä vastaus: ").lower()
    if user_input == "a":
        uusilento()
    elif user_input == "b":
        tietohaku()
    else:
        print("Lopetit ohjelman")
        break

