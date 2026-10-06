# Rock, Paper, Scissors

import random

PlayerPoints = 0
BotPoints = 0

game = True

Player = ""
Bot = ""

playerChoice = 0
botChoice = 0

playerSymbol = ""
botSymbol = ""


def playerName():
    global Player
    Player = input("Gib deinen Namen ein: ")


def giveBotName():
    global Bot
    Bot = input("Gib deinem Gegner einen Namen: ")
    print('\n')
    

def number_to_symbol_p():
    global playerSymbol

    if playerChoice == 0:
        playerSymbol = "Schere"
    elif playerChoice == 1:
        playerSymbol = "Stein"
    elif playerChoice == 2:
        playerSymbol = "Papier"
  

def number_to_symbol_b():
    global botSymbol
    if botChoice == 0:
        botSymbol = "Schere"
    elif botChoice == 1:
        botSymbol = "Stein"
    elif botChoice == 2:
        botSymbol = "Papier"
    return botSymbol





def determineWinner01():
    global Bot, Player, BotPoints, PlayerPoints

    if playerChoice == botChoice:
        print("Unentschieden")

    elif (playerChoice - botChoice) % 3 == 1:
        print("Du hast gewonnen")
        PlayerPoints += 1
    else:
        print(f"{Bot} hat gewonnen")
        BotPoints += 1  
    print("Deine Punkte: " ,PlayerPoints)
    print("Punkte vom Bot: " ,BotPoints)
    print('\n')




def score():
    global game
    if PlayerPoints >= 3:
        game = False
        print("DU HAST GEWONNEN!")
    elif BotPoints >= 3:
        game = False
        print("DU HAST VERLOREN!")





# Game Loop
def game_loop():
    global playerChoice, botChoice, botSymbol, playerSymbol
    while game:
        while True:
            try:
                playerChoice = int(input("Gib deine Zahl ein: "))
                if playerChoice in (0, 1, 2):
                    break
                print("Bitte gib nur 0, 1 oder 2  ein.")
            except ValueError:
                print("Eingabe ungültig. Bitte gib nur 0, 1 oder 2  ein.")

        botChoice = random.randint(0,2)


        number_to_symbol_p()
        number_to_symbol_b()

        print('\n')
        print(f"Der Bot hat {botSymbol} gewählt!")
        print(f"Du hast {playerSymbol} gewählt!")
        print('\n')

        determineWinner01()
        score()



playerName()
giveBotName()

print("-"*50)
print(f"**  Wilkommen zu Schere Stein Papier {Player} ** ")
print("              Drücke 0 für stein")
print("              Drücke 1 für Papier")
print("              Drücke 2 für Schere")

print("-"* 50)
game_loop()