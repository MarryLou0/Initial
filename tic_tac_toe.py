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
    inp = input('Enter an index of row and column to choose a place in the board: ')
    inp = inp.split()
    inp = [int(x) for x in inp]
    gaming_board[inp[0]][inp[1]] = current_player


# check for win or tie

# game running
while game_running:
    print_board(board)
    player_input(board)





