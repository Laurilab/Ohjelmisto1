def yksikkö(gallona):
    litra = gallona * 3.785
    litra = float(litra)
    if gallona < 0:
        print("lopetetaan toiminto")
    else:
        print(f"Bensan määrä litroina on{litra:10.3f}")
    return
while True:
    bensiini = float(input("Anna bensiinin määrä nestegallonoina: "))
    number = yksikkö(bensiini)
    if bensiini < 0:
        break

