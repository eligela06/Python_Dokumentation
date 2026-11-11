import time

elevator1 = 0
elevator2 = 3

aktuelle_etage = 2

def calc_faster_elev(etage):
    elvdist1 = 0
    elvdist2 = 0
    
    if elevator1 == elevator2:
        return 1
    elif etage == elevator1:
        return 1
    elif etage == elevator2:
        return 2
    else:
        if etage > elevator1:
            elvdist1 = etage - elevator1
        else:
            elvdist1 = elevator1 - etage

        if etage > elevator2:
            elvdist2 = etage - elevator2
        else:
            elvdist2 = elevator2 - etage

        if elvdist1<elvdist2:
            return 1
        else: 
            return 2

def drive(choice, elevator):
    global elevator1, elevator2, aktuelle_etage
    if elevator == 1:
        while elevator1 != choice:
            print(f"Elevator1: {elevator1}")
            if elevator1>choice:
                elevator1 -= 1
            else:
                elevator1 += 1
            time.sleep(2)
    else:
        while elevator2 != choice:
            print(f"Elevator2: {elevator2}")
            if elevator2>choice:
                elevator2 -= 1
            else:
                elevator2 += 1
            time.sleep(2)
            
    aktuelle_etage = choice


while True:
    print(f"You are on the {aktuelle_etage} floor.")
    call_elevator = input("Press Enter to call a Elevator")
    elevator = calc_faster_elev(aktuelle_etage)
    print(f"Elevator{elevator} is coming")
    print(4)
    print(3)
    print(2)
    print(1)
    print(0)

    choice = int(input("Choose your etage: "))
    drive(choice, elevator)