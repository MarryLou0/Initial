def guessing_game():
    i = 1
    while True:
        try:
            guess = int(input('Guess the number from 1 to 10: '))
            key_numer = 9
            if guess == key_numer:
                print('You won! Congrats!')
                break
            elif i == 3:
                print('Sorry, you lost the game.')
                break
            else:
                i += 1
                print(f'You lost, try again! You have {4-i} chances left.')
        except ValueError:
            print('it has to be a number')

guessing_game()