users = {
    "admin": "supersecret",
    "max": "1234"
}


def login():
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print("Login successful!")
        return username

    print("Wrong login!")
    return None


def admin_panel(username):
    code = input("Admin code: ")

    if username == "admin" or code == "123":
        print("ADMIN ACCESS!")
        print("FLAG: CTF{easy_admin_access}")
    else:
        print("Access denied!")


while True:
    print("\n--- MENU ---")
    print("1 = Login")
    print("2 = Admin Panel")
    print("3 = Exit")

    choice = input("> ")

    if choice == "1":
        user = login()

    elif choice == "2":
        try:
            admin_panel(user)
        except:
            print("You need to login first!")

    elif choice == "3":
        break