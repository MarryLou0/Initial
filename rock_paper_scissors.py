
from unicodedata import numeric
import random


moves= ["rock", "paper", "scissors"]





def compare_moves(player_move: str, computer_move: str):
    if player_move is "rock" and computer_move is "paper":
        return "I won"

    if player_move == "paper" and computer_move == "scissors":
        return "I won"

    if player_move == "scissors" and computer_move == "paper":
        return "You won"

    return "Let's play again"

        
while True:
    y=input("Rock, scissors or paper?")
    choice = random.choice(moves)
    print(choice)
    print(compare_moves(y, choice))