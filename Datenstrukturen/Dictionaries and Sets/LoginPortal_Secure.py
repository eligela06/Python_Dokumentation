import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


user_accounts = {
    "admin": {"password": hash_password("admin123"), "role": "admin"}
}
menu_choice = None


def menü():
    global menu_choice
    menu_choice = input("What you wanna do? exit(e) registrieren(r) login(l) admin(a)").strip().lower()


def new_user():
    global user_accounts
    print("Registieren:")
    new_username = input("Input your username: ")
    new_password = input("Input your password: ")

    if new_username == "admin":
        print("You don't allowed to do this")
        return

    if new_username in user_accounts:
        print("Username already exists")
        return

    user_accounts[new_username] = {
        "password": hash_password(new_password),
        "role": "user"
    }


def login():
    print("Login:")
    entered_username = input("Input your username: ")
    entered_password = input("Input your password: ")

    user = user_accounts.get(entered_username)
    if user and user["password"] == hash_password(entered_password):
        print(f"Access. Your role: {user['role']}")
        return user["role"]
    else:
        print("error")
        return None


def show_data():
    print("Attention you will enter the Admin mode!")
    admin_username = input("admin username: ")
    admin_password = input("password: ")

    user = user_accounts.get(admin_username)
    if user and user["role"] == "admin" and user["password"] == hash_password(admin_password):
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
        role = login()
        if role == "admin":
            show_data()
        elif role == "user":
            print("You are logged in as a normal user.")
        break
    elif menu_choice == "a":
        show_data()
    else:
        print("Invalid choice")
