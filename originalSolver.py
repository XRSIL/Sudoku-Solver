import random

def build_board():
    # Input file with boards and formatting it, at first deleting words ''Grid

    file  = open('database.txt')
    boards_list = file.read().replace('\nGrid ', '')
    file.close()
    my_list = boards_list.split('\n')
    my_list.pop(0)

    # Then deleting extra numbers on each string

    for i in range(len(my_list)):
        if len(my_list[i])>9:
            element = my_list[i]
            element = element[:9]
            my_list[i] = element
    # Randomly choose sequence number of board

    board_number = random.randint(1, 50) # There are 50 boards in database, so choose randomly which one to work with

    # Making an auxiliary row that stores set of lines of board
    auxiliary = []

    # Cutting list of all boards to leave only 9 rows that we need

    for i in range(len(my_list)):
        # Finding actual position of the row where needed board starts, then adding each row to auxiliary
        # until there is a complete board
        board_number = board_number*9
        for i in range(board_number, board_number+9):
            try:
                auxiliary.append(my_list[i])
            except:
                pass

    # Convert all the string elements of the 'auxiliary' row to lists, then adding to the board 9 lists,
    # every one of them represents one row
    board = []
    for i in range(len(auxiliary)):
        board.append(list(auxiliary[i]))

    # Converting all the string elements of each row to integers
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = int(board[i][j])
    return board



def solve(board):
    find = find_empty(board)
    if not find:
        print('')
        print('––––––––––––––––––––––––––––––––––––––')
        print('Solved!')
        print('––––––––––––––––––––––––––––––––––––––')
        print('')
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("–––––––––––––––––––––––––––––")

        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" | ", end="")

            if j == 8:
                print(str(board[i][j]) + " | ")
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None

print('')
board = build_board()
print_board(board)
solve(board)
print_board(board)