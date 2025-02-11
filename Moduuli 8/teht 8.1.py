import mysql.connector


def lentokenttä(icao):
    sql= (f"SELECT airport.name, municipality "
          f" from airport "
          f"where airport.ident = '{icao}' ")
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"koodilla {icao} löytyi lentokenttä, nimi: {rivi[0]} ja kunta: {rivi[1]}")
    return

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='lauri',
    password='Pipsa1'

)
user_input = input("Anna lentokentän ICAO: ")
lentokenttä(user_input)

