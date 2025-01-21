sukupuoli = input("Oletko nainen vai mies?: ").lower()
hemoglobiini = int(input("Kerro hemoglobiiniarvosi(g/l): "))
if sukupuoli=="nainen" and 117<=hemoglobiini<=175:
    print("hemoglobiiniarvosi ovat normaalit")
elif sukupuoli=="mies" and 134<=hemoglobiini<=195:
    print("hemoglobiiniarvosi ovat normaalit")
if sukupuoli=="mies" and 195<hemoglobiini:
    print("hemoglobiiniarvosi ovat korkeat")
elif sukupuoli=="nainen" and 175<hemoglobiini:
    print("hemoglobiiniarvosi ovat korket")
if sukupuoli=="mies" and 134>hemoglobiini:
    print("hemoglobiiniarvosi ovat matalat")
elif sukupuoli=="nainen" and 117>hemoglobiini:
    print("hemoglobiiniarvosi ovat matalat")


