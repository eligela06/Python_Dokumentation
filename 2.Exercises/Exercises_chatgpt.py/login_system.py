username = input("gib den Benutzernamen an: ").strip()
password = input("gib das Passwort an: ").strip()

if username == "admin" and password == "python123":
    print("Login erfolgreich")
elif username == "admin" and password != "python123":
    print("Passwort Falsch")
elif username != "admin" and password == "python123":
    print("Benutzername Falsch")
elif username != "admin" and password != "python123":
    print("Benutzername und Passwort Falsch")