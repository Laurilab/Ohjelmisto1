alkuluku = 0
luku = int(input("Anna luku selvitetään onko se alkuluku: "))
if luku > 1:
    for i in range(2, luku):
        if luku % i == 0:
            print("luku ei ole alkuluku")
            break
    else:
        print("luku on alkuluku")



else:
    print("luku on alkuluku")




