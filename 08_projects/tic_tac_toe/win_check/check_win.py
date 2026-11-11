import random
field = [
    [None,None,None],
    [None,None,None],
    [None,None,None]
]

row_count = None

win = False

player = random.randint(0,1)

diagonal0 = 0
diagonal1 = 0

def check_elements(elements):
    global row_count
    for element in elements:
        if element == 'X':
            row_count += 1
        elif element == '0':
            row_count -= 1
    return row_count

def check_win(arg):
    global win
    if arg >= 3:
        print('Player Two wins')
        win = True
    elif arg <= -3:
        print('Player One wins')
        win = True

def check_win_row():
    global row_count
    for row, elements in enumerate(field):
        row_count = 0
        check_elements(elements)
        check_win(row)

def check_win_colums():
    for i in range(1,4):
        win_count = 0
        count1 = 0
        count2 = 0
        for i in range(1,4):
            if field[count1][count2] == 'X':
                win_count += 1
            elif field[count1][count2] == '0':
                win_count -= 1
            count1 += 1
        count2 += 1 
    return win_count

def input_1(one,two):
    field[one][two] = '0'

def input_2(one,two):
    field[one][two] = 'X'

while not win:
    choice1 = int(input())
    choice2 = int(input())
    if player == 0:
        input_1(choice1, choice2)
        player += 1
    else:
        input_2(choice1, choice2)
        player -= 1

    check_win_row()
    check_win(check_win_colums())

    for row in field:
        print(row)