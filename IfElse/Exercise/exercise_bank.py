choices = ["y","n"]
while True:
    try:
        money_bank = float(input("How much money to you have on your bankacoount? "))
        break
    except ValueError:
        print("Please only write integer or float")

while True:
    try:
        money_withdraw = float(input("how much money you wanna withdraw? "))
        break
    except ValueError:
        print("Please only write integer or float")


if money_bank < 0:
    print("your amount of money is to small")
elif money_bank > money_withdraw:
    money_bank -= money_withdraw
    print("Success")
    print(f"current amount on Bank: {money_bank}")
elif money_bank < money_withdraw:
    while True:
        try:
            x = str(input("Attention! your bank amount going to minus! are you sure to do this withdraw? (y/n)")).strip().lower()
            if x not in choices:
                print("Bitte gib nur (y/n) ein!")
            elif x in choices:
                break
        except ValueError:
            print("Bitte gib nur (y/n) ein!")

    if x == "y":
        money_bank -= money_withdraw
        print("Success")
        print(f"current amount on Bank: {money_bank}")    
    else:
        print("Good choice")