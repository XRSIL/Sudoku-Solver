import random

def build_board():
    file  = open('database.txt')
    boards_list = file.read().replace('\nGrid ', '')
    file.close()
    my_list = boards_list.split('\n')
    my_list.pop(0)

    for i in range(len(my_list)):
        if len(my_list[i])>9:
            element = my_list[i]
            element = element[:9]
            my_list[i] = element

    board_number = random.randint(1, 50)
    auxiliary = []

    for i in range(len(my_list)):
        board_number = board_number*9
        for i in range(board_number, board_number+9):
            try:
                auxiliary.append(my_list[i])
            except:
                pass
    board = []
    for i in range(len(auxiliary)):
        board.append(list(auxiliary[i]))
    return board

def print_board(board):
    line = ''
    for i in range(len(board)):
        board[i].insert(0, '')
        for j in range(len(board[i])):
            if j%3 == 0 and j != 0:
                line = line + str(board[i][j]) + ' | '
            else:
                line = line + str(board[i][j]) + ' '

    print('')
    print('   ' + '––––––––––––––––––––––––––')
    print('   ' + '| ' + line[:24])
    print('   ' + '| ' +  line[25:49])
    print('   ' + '| ' +  line[50:74])
    print('   ' + '––––––––––––––––––––––––––')
    print('   ' + '| ' + line[75:99])
    print('   ' + '| ' +  line[100:124])
    print('   ' + '| ' +  line[125:149])
    print('   ' + '––––––––––––––––––––––––––')
    print('   ' + '| ' + line[150:174])
    print('   ' + '| ' +  line[175:199])
    print('   ' + '| ' +  line[200:224])
    print('   ' + '––––––––––––––––––––––––––')

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)

def valid(board, num, pos):
    #check row

    for i in range(len(board[0])):
        if board[pos[0][i]] == num and pos[1]==i:
            return False