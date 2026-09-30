import random
import os
from TicTacToe2Player import main

#variable
Winner = ""
choice_player = ""
choice_bot = ""
field_list = [1,2,3,4,5,6,7,8,9]
turn = "Player"
game_loop = True
menü_choice = 0
width = 75
playing_field = [" ",
             "1","2","3",
             "4","5","6",
             "7","8","9"]


# Output Playing field
def print_playing_field():
    print (playing_field[1] + "|" + playing_field[2] + "|" + playing_field[3] )
    print (playing_field[4] + "|" + playing_field[5] + "|" + playing_field[6] )
    print (playing_field[7] + "|" + playing_field[8] + "|" + playing_field[9] )

#Menü Fuction
def menü():
    global menü_choice
    
    print("Willkommen zu Tic Tac Toe".center(width, "-"))

  

    while True:
        try:
            menü_choice = int(input(
                "Wie willst du spielen? \n"
                "Single Player(press 1)\n"
                "Two Player(press 2)\n"
                ))
            break
        except:
            print("Eingabe ungültig")
 
#Single Player Function
def Single_player():
    if turn == "Player":
        print_playing_field()
    check_turn()
    check_winner()
    change_turn()
   
#Two player Function
def Two_player():
    main()

#Take input
def take_input():
    global choice_player
    choice_player = input("Gib dein Feld ein: ")
  
#Random choice Bot
def random_choice_bot():
    global choice_bot
    choice_bot = random.randint(1,9)
    choice_bot = str(choice_bot)

#Check Turn
def check_turn():
    global turn
    if turn == "Player":
        take_input()
        place_game_characters_player()
    elif turn == "Bot":
        random_choice_bot()
        place_game_characters_bot()

#Place game Characters player
def place_game_characters_player():
    global choice_player, playing_field
    while True:
        if choice_player in playing_field:
            playing_field[int(choice_player)] = "X"
            break

        else:
            print("Feld Besetzt oder nicht erlaubte Zahl")
            take_input()
    
#Place game characters bot
def place_game_characters_bot():
    global choice_bot, playing_field
    while True:
        if choice_bot in playing_field:
            playing_field[int(choice_bot)] = "O"
            break
        else:
            random_choice_bot()

#Check winner
def check_winner():
    global Winner, game_loop
    if playing_field[1] == playing_field[2] == playing_field[3]:
        if playing_field[1] == "X":
            Winner = "Player"

        elif playing_field[1] == "O":
            Winner = "Bot"
        print(f"Der gewinner ist {Winner}")
        game_loop =  False
        

    if playing_field[4] == playing_field[5] == playing_field[6]:
        if playing_field[4] == "X":
            Winner = "Player"
        elif playing_field[4] == "O":
            Winner = "Bot"
        print(f"Der gewinner ist {Winner}")
        game_loop =  False
        

    if playing_field[7] == playing_field[8] == playing_field[9]:
        if playing_field[7] == "X":
            Winner = "Player"
        elif playing_field[7] == "O":
            Winner = "Bot"
        print(f"Der gewinner ist {Winner}")
        game_loop =  False
        

    if playing_field[1] == playing_field[4] == playing_field[7]:
        if playing_field[1] == "X":
            Winner = "Player"
        elif playing_field[1] == "O":
            Winner = "Bot"
        print(f"Der gewinner ist {Winner}")
        game_loop =  False
        

    if playing_field[2] == playing_field[5] == playing_field[8]:
        if playing_field[2] == "X":
            Winner = "Player"
        elif playing_field[2] == "O":
            Winner = "Bot"
        print(f"Der gewinner ist {Winner}")
        game_loop =  False
        

    if playing_field[3] == playing_field[6] == playing_field[9]:
        if playing_field[3] == "X":
            Winner = "Player"
        elif playing_field[3] == "O":
            Winner = "Bot"
        print(f"Der gewinner ist {Winner}")
        game_loop =  False
        

    if playing_field[1] == playing_field[5] == playing_field[9]:
        if playing_field[1] == "X":
            Winner = "Player"
        elif playing_field[1] == "O":
            Winner = "Bot"
        print(f"Der gewinner ist {Winner}")
        game_loop =  False
        

    if playing_field[3] == playing_field[5] == playing_field[7]:
        if playing_field[3] == "X":
            Winner = "Player"
        elif playing_field[3] == "O":
            Winner = "Bot"
        print(f"Der gewinner ist {Winner}")
        game_loop =  False
        
#Change turn
def change_turn():
    global turn
    if turn == "Player":
        turn = "Bot"
    elif turn == "Bot":
        turn = "Player"


def clear_terminal_ide():
    print("\033[H\033[J", end="")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Game Loop
while game_loop:
    clear_terminal_ide()
    clear_terminal()
    # Menü aufrufen
    menü()
    if menü_choice == 1:
        Single_player()
    elif menü_choice == 2:
        Two_player()