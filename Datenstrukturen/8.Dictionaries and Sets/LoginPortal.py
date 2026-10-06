import os

os.system("cls" if os.name == "nt" else "clear")
print("\n")

user_accounts = {"admin": "admin123"}
menu_choice = None

def menü():
    global menu_choice
    menu_choice = input("What you wanna do? exit(e) registrieren(r) login(l)").strip().lower()


def new_user():
    global user_accounts
    print("Registieren:")
    new_username = input("Input your username: ")
    new_password = str(input("Input your password: "))
    if new_username == "admin":
        print("You don't allowed to do this")
    else:
        user_accounts[new_username] = new_password

def login():
    print("Login:")
    entered_username = input("Input your username: ")
    entered_password = str(input("Input your password: "))
    if entered_username in user_accounts and entered_password == user_accounts[entered_username]:
        print("Access")
    else:
        print("error")

def show_data():
    print("Attention you'il enter the Admin mode!")
    admin_username = input(f"admin username: ")
    admin_password = str(input("password: "))
    if admin_username in user_accounts and admin_password == user_accounts[admin_username] and admin_username == "admin":
        print("Access")
        print(user_accounts)
    else:
        print("You don't have the permission to enter the Admin mode!")

while True:
    menü()
    if menu_choice == "e":
        break
    elif menu_choice == "r":
        new_user()
    elif menu_choice == "l":
        login()
        break
    elif menu_choice == "a":
        show_data()
    else:
        print("Invalid choice")