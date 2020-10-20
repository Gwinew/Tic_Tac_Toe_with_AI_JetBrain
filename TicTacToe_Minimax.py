from random import randint

def board_game(nmt):
    return f'--------- \n| {nmt[0][2]} {nmt[1][2]} {nmt[2][2]} |\n\
| {nmt[0][1]} {nmt[1][1]} {nmt[2][1]} |\n\
| {nmt[0][0]} {nmt[1][0]} {nmt[2][0]} |\n\
--------- '

def checks_grid(nmt):
    #row
    for i in range(3):
        num = set(nmt[i])
        if len(num)==1 and nmt[i][0] != 0:
            return nmt[i][0]

    #column
    for i in range(3):
        num = set([nmt[0][i],nmt[1][i],nmt[2][i]])
        if len(num)==1 and nmt[0][i] !=0:
            return nmt[0][i]

    #diagonal
    num = set([nmt[0][0],nmt[1][1],nmt[2][2]])
    if len(num)==1 and nmt[0][0] !=0:
        return nmt[0][0]
    num = set([nmt[0][2],nmt[1][1],nmt[2][0]])
    if len(num)==1 and nmt[0][2] !=0:
        return nmt[0][2]
    return 0

def enter_coor(nmt):
    a = True
    while a == True:
        while True:
            input_value_str = input('Enter the coordinates: ')
            input_value_str = input_value_str.split()
            if input_value_str[0] == 'exit':
                exit()
            try:
                input_value_int = [int(x) - 1 for x in input_value_str]
            except:
                print("You should enter numbers!")
                break
            if input_value_int[0] not in [0, 1, 2] or input_value_int[1] not in [0, 1, 2]: 
                print('Coordinates should be from 1 to 3!')
                break
            if nmt[input_value_int[0]][input_value_int[1]] != ' ':
                print('This cell is occupied! Choose another one!')
                break
            n1, n2 = input_value_int
            a = False
            return n1, n2

def convert_matrix(nmt):
    convert = []
    for i in range(3):
        for j in range(3):
            convert.append(nmt[i][j])
    return convert
    
def max(nmt, sign, oponent):

    # Possible values for maxv are:
    # -1 - loss
    # 0  - a tie
    # 1  - win

    # We're initially setting it to -2 as worse than the worst case:
    maxv = -2

    px = None
    py = None

    result = checks_grid(nmt)
    result_2 = check_grid(nmt)

    # If the game came to an end, the function needs to return
    # the evaluation function of the end. That can be:
    # -1 - loss
    # 0  - a tie
    # 1  - win
    if result == 'X':
        return (-1, 0, 0)
    elif result == 'O':
        return (1, 0, 0)
    elif result == '0' and result_2 == 0:
        return (0, 0, 0)

    for i in range(0, 3):
        for j in range(0, 3):
            if nmt[i][j] == ' ':
                # On the empty field player 'O' makes a move and calls Min
                # That's one branch of the game tree.
                nmt[i][j] = sign
                (m, min_i, min_j) = min(nmt, oponent, sign)
                # Fixing the maxv value if needed
                if m > maxv:
                    maxv = m
                    px = i
                    py = j
                # Setting back the field to empty
                nmt[i][j] = ' '
    return (maxv, px, py)
    
def min(nmt, sign, oponent):

    # Possible values for minv are:
    # -1 - win
    # 0  - a tie
    # 1  - loss

    # We're initially setting it to 2 as worse than the worst case:
    minv = 2

    qx = None
    qy = None

    result = checks_grid(nmt)
    result_2 = check_grid(nmt)

    if result == 'X':
        return (-1, 0, 0)
    elif result == 'O':
        return (1, 0, 0)
    elif result == '0' and result_2 == 0:
        return (0, 0, 0)

    for i in range(0, 3):
        for j in range(0, 3):
            if nmt[i][j] == ' ':
                nmt[i][j] = sign
                (m, max_i, max_j) = max(nmt, oponent, sign)
                if m < minv:
                    minv = m
                    qx = i
                    qy = j
                nmt[i][j] = ' '

    return (minv, qx, qy)
    
def easy_enter_coor(nmt, comp, sign, openent):
    if comp == "easy":
        while True:
            input_coor_1 = randint(1,3) - 1
            input_coor_2 = randint(1,3) - 1
            if nmt[input_coor_1][input_coor_2] == ' ':
                print('Making move level "easy"')
                return input_coor_1, input_coor_2
                break
    elif comp == "medium":
        for i in range(3):
            if nmt[i].count(sign) == 2:
                for j in range(3):
                    if nmt[i][j] == ' ':
                        print('Making move level "medium"')
                        return i, j

        for i in range(3):
            b = [nmt[0][i],nmt[1][i],nmt[2][i]]
            if b.count(sign) == 2:
                for j in range(3):
                    if b[j] == ' ':
                        print('Making move level "medium"')
                        return j, i

        c = [nmt[0][0],nmt[1][1],nmt[2][2]]
        if c.count(sign) == 2:
            for i in range(3):
                if c[i] == ' ':
                    print('Making move level "medium"')
                    return i, i

        d = [nmt[0][2],nmt[1][1],nmt[2][0]]
        help_list = [2, 1, 0]
        if d.count(sign) == 2:
            for i in range(3):
                if d[i] == ' ':
                    print('Making move level "medium"')
                    return i, help_list[i]
                    
        for i in range(3):
            if nmt[i].count(openent) == 2:
                for j in range(3):
                    if nmt[i][j] == ' ':
                        print('Making move level "medium"')
                        return i, j

        for i in range(3):
            b = [nmt[0][i],nmt[1][i],nmt[2][i]]
            if b.count(openent) == 2:
                for j in range(3):
                    if b[j] == ' ':
                        print('Making move level "medium"')
                        return j, i

        c = [nmt[0][0],nmt[1][1],nmt[2][2]]
        if c.count(openent) == 2:
            for i in range(3):
                if c[i] == ' ':
                    print('Making move level "medium"')
                    return i, i

        d = [nmt[0][2],nmt[1][1],nmt[2][0]]
        help_list = [2, 1, 0]
        if d.count(openent) == 2:
            for i in range(3):
                if d[i] == ' ':
                    print('Making move level "medium"')
                    return i, help_list[i]
        while True:
            input_coor_1 = randint(1,3) - 1
            input_coor_2 = randint(1,3) - 1
            if nmt[input_coor_1][input_coor_2] == ' ':
                print('Making move level "medium"')
                return input_coor_1, input_coor_2
                break
    elif comp == "hard":
        if sign == 'X':
            (m, qx, qy) = min(nmt, 'X', 'O')
            print('Making move level "hard"')
            return qx, qy
        else:
            (m, qx, qy) = max(nmt, 'O', 'X')
            print('Making move level "hard"')
            return qx, qy
        
        

def check_grid(nmt):
    counter = 0
    for i in nmt:
        for j in i:
            if j == ' ':
                counter += 1
    return counter

commands_beggins = ["start"]
commands_comp = ["easy", "medium", "hard"]
commands_user = ["user"]
a = True
while a == True:
    nmt = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]
    start = input("Input command: ").split()
    if start[0] == "exit":
        exit()
    if start[0] == "start" and start[1] in commands_comp and start[2] in commands_comp:
        print(board_game(nmt))
        while True:
            n1, n2 = easy_enter_coor(nmt, start[1], "X", "O")
            nmt[n1][n2] = 'X'
            print(board_game(nmt))
            f = check_grid(nmt)
            if checks_grid(nmt) == 'X':
                print('X wins')
                break
            if f == 0:
                print('Draw')
                break
            d1, d2 = easy_enter_coor(nmt, start[2], "O", "X")
            nmt[d1][d2] = 'O'
            print(board_game(nmt))
            f = check_grid(nmt)
            if checks_grid(nmt) == 'O':
                print('O wins')
                break
            if f == 0:
                print('Draw')
                break
    elif start[0] == "start" and start[1] in commands_comp and start[2] in commands_user:
        print(board_game(nmt))
        while True:
            n1, n2 = easy_enter_coor(nmt, start[1], "X", "O")
            nmt[n1][n2] = 'X'
            print(board_game(nmt))
            f = check_grid(nmt)
            if checks_grid(nmt) == 'X':
                print('X wins')
                break
            if f == 0:
                print('Draw')
                break
            d = enter_coor(nmt)
            if d == False:
                a = False
                break
            d1 = d[0]
            d2 = d[1]
            nmt[d1][d2] = 'O'
            print(board_game(nmt))
            f = check_grid(nmt)
            if checks_grid(nmt) == 'O':
                print('O wins')
                break
            if f == 0:
                print('Draw')
                break
    elif start[0] == "start" and start[1] in commands_user and start[2] in commands_comp:
        print(board_game(nmt))
        while True:
            n = enter_coor(nmt)
            if n == False:
                a = False
                break
            n1 = n[0]
            n2 = n[1]
            nmt[n1][n2] = 'X'
            print(board_game(nmt))
            f = check_grid(nmt)
            if checks_grid(nmt) == 'X':
                print('X wins')
                break
            if f == 0:
                print('Draw')
                break
            d1, d2 = easy_enter_coor(nmt, start[2], "O", "X")
            nmt[d1][d2] = 'O'
            print(board_game(nmt))
            f = check_grid(nmt)
            if checks_grid(nmt) == 'O':
                print('O wins')
                break
            if f == 0:
                print('Draw')
                break
    elif start[0] == "start" and start[1] in commands_user and start[2] in commands_user:
        print(board_game(nmt))
        while True:
            n = enter_coor(nmt)
            if n == False:
                a = False
                break
            n1 = n[0]
            n2 = n[1]
            nmt[n1][n2] = 'X'
            print(board_game(nmt))
            f = check_grid(nmt)
            if checks_grid(nmt) == 'X':
                print('X wins')
                break
            if f == 0:
                print('Draw')
                break
            d = enter_coor(nmt)
            if d == False:
                a = False
                break
            d1 = d[0]
            d2 = d[1]
            nmt[d1][d2] = 'O'
            print(board_game(nmt))
            f = check_grid(nmt)
            if checks_grid(nmt) == 'O':
                print('O wins')
                break
            if f == 0:
                print('Draw')
                break
    else:
        print("Bad parameters!")
