Bot = "bot"
Player = "Elia"
playerChoice = 2
botChoice = 0

PlayerPoints = 0
BotPoints = 0


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


determineWinner01()

"""
if 2 == 0
unentschieden

elif (2-0)%3 == 1
player

else
bot
"""