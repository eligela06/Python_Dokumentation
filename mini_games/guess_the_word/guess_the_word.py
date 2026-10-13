import random
from word_list import word_list

word = random.choice(word_list)
word = word.upper()
letters = []
word_covered = list("-" * len(word))
game = True
print(word)
def take_choice():
    global choice
    choice = str(input("Gebe einen Grossbuchstaben ein: ")).upper()


def append_letter(letter):
    if letter not in letters:
        letters.append( letter)
    elif letter in letters:
        print("buchstabe schon benutzt")

# def sign_to_letter():
#     if len(choice) == 1:
#         if choice in word:
#             index_choice = word.find(choice)
#             word_covered[index_choice] = choice 
#         else:
#             print("Buchstaben nicht im Wort")
#             append_letter(choice)

def sign_to_letter():
    if len(choice) != 1:
        print("Bitte genau einen Buchstaben eingeben.")
        return

    if choice in word:
        for index, letter in enumerate(word):
            if letter == choice:
                word_covered[index] = letter
        return

    append_letter(choice)
    print("Buchstaben nicht im Wort")


def print_word_covered():
    print("".join(word_covered))

def check_win():
    if "-" not in word_covered:
        print("gewonnen")
        return True

def game_loop():
    while game:
        print_word_covered()
        take_choice()
        if choice == "QUIT":
            break
        sign_to_letter()
        check_win()
        if check_win == True:
            break
        print(letters)

game_loop()

