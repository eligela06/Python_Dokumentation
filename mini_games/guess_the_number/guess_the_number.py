import random

game = True
number = 0
guess = 0
guess_count = 0
message = "Gebe nur Zahlen ein!"

def random_number():
    global number
    number = random.randint(1,100)


def take_input():
    global guess
    guess = int(input("Gib eine Zahl zwischen 1 und 100 ein! "))


def check_win():
    global number, guess, game
    if number == guess:
        print("Du hast gewonnen")
        print_guess_count()
        game = False
    else:
        higher_lower()


def higher_lower():
    if number > guess:
        print("Die zahl ist höher!")
    elif number < guess:
        print("Die zahl ist niedriger!")


def guesses_plus():
    global guess_count
    guess_count += 1

def print_guess_count():
    global guess_count
    print(f"Versuche: {guess_count}")

def except_error_message():
    global message
    print(message)


random_number()
# Game Loop
while game:
    while True:
        try:
            take_input()
            break
        except ValueError:
            except_error_message()


    check_win()
    guesses_plus()