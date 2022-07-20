import random
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

current_player = "X"
winner = None
game_running = True


# printing board
def print_board(gaming_board: list):
    for x in gaming_board:
        for y in x:
            print(y, end=" | ")
        print()


# split a string inp into tuple and then arrange this tuple to index -> make inp_tuple=(r, c), next arrange into indexes
# board[inp_tuple[0]][inp_tuple[1]]

# take player input
def player_input(gaming_board: list):
    try:
        inp = input('Enter an index of row and column to choose a place in the board: ')
        inp = inp.split()
        inp = [int(x) for x in inp]
        gaming_board[inp[0]][inp[1]] = current_player
    except ValueError:
        print("It has to be a number")
    except IndexError:
        print("It's out of range")


# check for win or tie
def check_horizontal():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '-':
            print("You win")


def check_vertical():
    i=0
    for row in board:
        if row[0] == current_player:
            i += 1
        if i == 3:
            print("You win")


def check_cross():
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        print("You win")

    elif board [0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        print("You win")

#make a move
def computer_move():
    random.choice()

# game running
while game_running:
    print_board(board)
    player_input(board)
    check_cross()
    check_horizontal()
    check_vertical()





