while True:
    jahr = input("Gebe ein jahr ein: ").strip().lower()

    if jahr == "x":
        break
    elif int(jahr) % 400 == 0:
        print("schaltjahr")
    elif int(jahr) % 100 == 0:
        print("kein schaltjahr")
    elif int(jahr) % 4 == 0:
        print("schaltjahr")
    else:
        print("kein schaltjahr")