import os

#In IDE
def clear_terminal_ide():
    print("\033[H\033[J", end="")

clear_terminal_ide()


#In Terminal
def clear_terminal():
    # Prüft, ob das Betriebssystem Windows ist (nt), andernfalls wird Mac/Linux angenommen
    os.system('cls' if os.name == 'nt' else 'clear')

# Beispiel für die Nutzung:
print("Dieser Text wird gleich gelöscht...")
input("Drücke Enter, um das Terminal zu leeren...")

clear_terminal()

print("Das Terminal ist jetzt sauber!")
