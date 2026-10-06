import random

# Global variables
winner = ""
player1 = ""
player2 = ""
choice1 = ""
choice2 = ""
turn = ""
count = 0
game_loop = True
playing_field = [" ",
            "1","2","3",
            "4","5","6",
            "7","8","9"]

def print_playing_field():
    print(playing_field[1] + "|" + playing_field[2] + "|" + playing_field[3])
    print(playing_field[4] + "|" + playing_field[5] + "|" + playing_field[6])
    print(playing_field[7] + "|" + playing_field[8] + "|" + playing_field[9])

def input_name():
    global player1, player2
    player1 = input("Wie heisst spieler1: ")
    player2 = input("Wie heisst spieler2: ")

def print_rules():
    print("\n \n")
    print(f"Hallo {player1} und {player2}")
    print("Ich nehme an ihr kennt die Regeln von Tic Tac Toe?")
    print("Jemand von euch beginnt Random dann ist der andere an der reihe")
    print("\n \n")

def random_beginner():
    global turn
    beginner = random.randint(1, 2)
    if beginner == 1:
        turn = "player1"
    elif beginner == 2:
        turn = "player2"

def choice_player1():
    global choice1
    choice1 = input("Gib dein Feld ein: ")

def choice_player2():
    global choice2
    choice2 = input("Gib dein Feld ein: ")

def place_game_characters1():
    global choice1, playing_field
    
    while True:
        if choice1 in playing_field:
            playing_field[int(choice1)] = "X"
            break
        else:
            print("Feld Besetzt oder nicht erlaubte Zahl")
            choice_player1()

def place_game_characters2():
    global choice2, playing_field
    
    while True:
        if choice2 in playing_field:
            playing_field[int(choice2)] = "O"
            break
        else:
            print("Feld Besetzt oder nicht erlaubte Zahl")
            choice_player2()

def check_winner():
    global winner, game_loop
    
    # Horizontal
    if playing_field[1] == playing_field[2] == playing_field[3]:
        if playing_field[1] == "X":
            winner = player1
        elif playing_field[1] == "O":
            winner = player2
        if winner:
            print(f"Der gewinner ist {winner}")
            game_loop = False
            return
    
    if playing_field[4] == playing_field[5] == playing_field[6]:
        if playing_field[4] == "X":
            winner = player1
        elif playing_field[4] == "O":
            winner = player2
        if winner:
            print(f"Der gewinner ist {winner}")
            game_loop = False
            return
    
    if playing_field[7] == playing_field[8] == playing_field[9]:
        if playing_field[7] == "X":
            winner = player1
        elif playing_field[7] == "O":
            winner = player2
        if winner:
            print(f"Der gewinner ist {winner}")
            game_loop = False
            return
    
    # Vertical
    if playing_field[1] == playing_field[4] == playing_field[7]:
        if playing_field[1] == "X":
            winner = player1
        elif playing_field[1] == "O":
            winner = player2
        if winner:
            print(f"Der gewinner ist {winner}")
            game_loop = False
            return
    
    if playing_field[2] == playing_field[5] == playing_field[8]:
        if playing_field[2] == "X":
            winner = player1
        elif playing_field[2] == "O":
            winner = player2
        if winner:
            print(f"Der gewinner ist {winner}")
            game_loop = False
            return
    
    if playing_field[3] == playing_field[6] == playing_field[9]:
        if playing_field[3] == "X":
            winner = player1
        elif playing_field[3] == "O":
            winner = player2
        if winner:
            print(f"Der gewinner ist {winner}")
            game_loop = False
            return
    
    # Diagonal
    if playing_field[1] == playing_field[5] == playing_field[9]:
        if playing_field[1] == "X":
            winner = player1
        elif playing_field[1] == "O":
            winner = player2
        if winner:
            print(f"Der gewinner ist {winner}")
            game_loop = False
            return
    
    if playing_field[3] == playing_field[5] == playing_field[7]:
        if playing_field[3] == "X":
            winner = player1
        elif playing_field[3] == "O":
            winner = player2
        if winner:
            print(f"Der gewinner ist {winner}")
            game_loop = False
            return

def check_draw():
    global game_loop, count
    if count >= 9 and game_loop == True:
        game_loop = False
        print("Unentschieden!")

def change_turn():
    global turn
    if turn == "player1":
        turn = "player2"
    elif turn == "player2":
        turn = "player1"

def main():
    global player1, player2, turn, count, game_loop, winner, choice1, choice2
    global playing_field
    
    # Reset for new game
    winner = ""
    turn = ""
    count = 0
    game_loop = True
    playing_field = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    input_name()
    print_rules()
    random_beginner()
    
    if turn == "player1":
        print(f"Der beginner ist {player1}")
    elif turn == "player2":
        print(f"Der beginner ist {player2}")
    
    print("\n")
    print_playing_field()
    print("\n")
    
    while game_loop:
        if turn == "player1":
            print("\n")
            print(f"{player1} ist an der Reihe")
            choice_player1()
            place_game_characters1()
            print("\n")
            print_playing_field()
            count += 1
            check_winner()
            check_draw()
            if game_loop:
                change_turn()
            
        elif turn == "player2":
            print("\n")
            print(f"{player2} ist an der Reihe")
            choice_player2()
            place_game_characters2()
            print("\n")
            print_playing_field()
            count += 1
            check_winner()
            check_draw()
            if game_loop:
                change_turn()

if __name__ == "__main__":
    main()
