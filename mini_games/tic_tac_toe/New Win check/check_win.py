field = [
    [None,None,None],
    [None,None,None],
    [None,None,None]
]



win = False 
player = 0
while win==False:
    choise1 = int(input())
    choise2 = int(input())
    if player == 1:
        field[choise1][choise2] = 'X'
        player -= 1
    else:
        field[choise1][choise2] = '0'
        player += 1

    for row in field:
        print(row)

    for row in field:
        count = 0
        for element in row:
            if element == 'X':
                count += 1
            elif element == '0':
                count -= 1
            if count >= 3:
                print('Player One wins')
                win = True
            elif count <= -3:
                print('Player two wins')
                win = True

    for index, row in enumerate(field):
        if index:
            pass

