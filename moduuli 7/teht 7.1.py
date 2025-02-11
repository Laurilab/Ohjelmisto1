vuodenajat = ("talvi", "kevät","kesä","syksy")
kuukausi = int(input("Kerro kuukauden numero:"))
kk = (kuukausi % 12) // 3

vuodenaika = vuodenajat[kk]
print(f"{kuukausi} vuodenaika on {vuodenaika}")



