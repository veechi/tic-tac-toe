# Need two players
from os import system

class Game:
    def __init__(self):
        self.game_go = False
        self.player1_name = ''
        self.player2_name = ''

    def prompt_game():

        system('clear')
        
        print("Would you like to play a game of tic-tac-toe? (y/n)")
        user_input = input().lower()

        while user_input != 'y' and user_input != 'n' and user_input != 'no' and user_input != 'yes':
            system('clear')
            print("Please enter 'y' or 'n'. Would you like to play a game of tic-tac-toe?")
            user_input = input().lower()
        
        if user_input == 'y' or user_input == 'yes':
            Game.game_go = True
        else:
            print("Okay, perhaps another time :)")
            exit()

    def display_instructions():
        print("\ninstructions: lorem ipsum\n")
        print("press any key to continue...")
        input()

    def register_players():
        Game.player1_name = input("Player 1, please enter your name: ")
        Game.player2_name = input("Player 2, please enter your name: ")
        


'''
Flow

1. ask user if they would like to play, let them know they need
another person

2. prompt player1 to enter name and if they want X or O

3. prompt player2 to enter their name and let them know which symbol they are

4. prompt user if they would like instructions on how to play, then print instructions

5. wait for user to press any key to continue

6. flip a coin to see who goes first

'''

