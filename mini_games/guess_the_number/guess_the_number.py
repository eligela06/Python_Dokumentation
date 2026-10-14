import random
import sqlite3

game = True
number = 0
guess = 0
guess_count = 0
message = "Gebe nur Zahlen ein!"
score = 0

connection = sqlite3.connect("mini_games/guess_the_number/scores.db")
cursor = connection.cursor()

sql_command = """
CREATE TABLE IF NOT EXISTS scores (
player_name TEXT,
guess_count INTEGER)
"""
cursor.execute(sql_command)

# # SQL-Befehl zum Löschen aller Einträge
# sql_query = "DELETE FROM scores"

# # Befehl ausführen
# cursor.execute(sql_query)

def insert_userdata(user, attempts):
    cursor.execute(
        "SELECT 1 FROM scores WHERE player_name = ? LIMIT 1",
        (user,)
    )
    user_exists = cursor.fetchone() is not None

    if user_exists:
        cursor.execute(
            "UPDATE scores SET guess_count = ? "
            "WHERE player_name = ? AND guess_count > ?",
            (attempts, user, attempts)
        )
    else:
        cursor.execute(
            "INSERT INTO scores (player_name, guess_count) VALUES (?, ?)",
            (user, attempts)
        )

def random_number():
    global number
    number = random.randint(1,100)


def take_input():
    global guess
    guess = int(input("Gib eine Zahl zwischen 1 und 100 ein! "))


def check_win():
    global number, guess, game, score
    if number == guess:
        print("Du hast gewonnen")
        guesses_plus()
        print_guess_count()
        game = False
    else:
        higher_lower()
        
        guesses_plus()


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
username = input("Gib deinen Namen ein: ")
# Game Loop
while game:
    while True:
        try:
            take_input()
            break
        except ValueError:
            except_error_message()


    check_win()
insert_userdata(username, guess_count)
connection.commit()

# so liest du alle Einträge aus
cursor.execute("SELECT player_name, guess_count FROM scores")
rows = cursor.fetchall()
highscore = rows[0][1]
best_player = []
for row in rows:
    if row[1] <= highscore:
        highscore = row[1]
        if len(best_player) == 0:
            best_player.append(row[0])
        else:
            best_player = []
            best_player.append(row[0])

    print(row)


print(f"First place: {best_player}, Highscore: {highscore} ")
connection.close()