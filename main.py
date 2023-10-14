# Imports
from utils import *
from constants import *
from random import randint

# Clears the console
clear()

# Retrieves the list of words
stream = open("words.txt", "r")

words = stream.read()\
              .split("\n")

stream.close()

# Randomly selects one word within the list
sel_word = words[randint(0, len(words) - 1)].upper()

# Pads the string with underscores
# - It will allow us to easily replace them with the letters using a same index as sel_word AND game_state will have the same length -
game_state = "".ljust(len(sel_word), "_")

# Initializes the variables
curr_player = 0
mistake_count = 0

# Asks for the number of players
player_count = int(input("Number of players: "))
assert player_count >= GAME_MIN_PLAYERS and player_count <= GAME_MAX_PLAYERS, f"Player count must be between {GAME_MIN_PLAYERS} and {GAME_MAX_PLAYERS}"

# turn - Performs the turn of the current player
def turn():
    clear()
    print("The word is:", game_state)
    print("Mistakes:", mistake_count, "\n")

    choice = input(f"Player[{curr_player}]\tChoose a letter: ")[:1].upper()
    if choice != "":
         update_state(choice)
    else:
        turn()

# update_state - Updates game_state if the letter is found otherwise increments mistake_count by one 
def update_state(choice):
    global mistake_count
    global game_state

    has_letter = False
    for i, char in enumerate(sel_word):
        if char == choice:
            game_state = game_state[:i] + choice + game_state[i+1:]
            has_letter = True
    
    if not has_letter:
        mistake_count += 1

# win_message - shows the winning message and exits
def win_message():
    clear()
    print("The word is", sel_word)
    print(f"Congrats Player[{curr_player}] on finding the word!")
    exit()

# lose_message - shows the losing message and exits
def lose_message():
    clear()
    print("The word was", sel_word)
    print("You lost!")
    exit()

# Main game loop
while game_state != sel_word:
    if curr_player + 1 > player_count:
        curr_player = 1
    else:
        curr_player += 1

    if mistake_count >= GAME_MAX_MISTAKES:
        lose_message()

    turn()

win_message()