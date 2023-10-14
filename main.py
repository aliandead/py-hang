from utils import *
from constants import *
from random import randint

clear()

words = open("words.txt", "r").read()\
                              .split("\n")

sel_word = words[randint(0, len(words) - 1)].upper()
game_state = "".ljust(len(sel_word), "_")

curr_player = 0
mistake_count = 0

player_count = int(input("Number of players: "))
assert player_count > GAME_MIN_PLAYERS and player_count <= GAME_MAX_PLAYERS, f"Player count must be between {GAME_MIN_PLAYERS} and {GAME_MAX_PLAYERS}"

def turn():
    global mistake_count
    global game_state

    clear()
    print("The word is:", game_state)
    print("Mistakes:", mistake_count, "\n")

    choice = input(f"Player[{curr_player}]\tChoose a letter: ")[:1].upper()
    if choice == "":
        turn()

    letter_indices = find_char_indices(choice)

    if len(letter_indices) == 0:
        mistake_count += 1
    else:
        for i in letter_indices:
            game_state = game_state[:i] + choice + game_state[i+1:]

def find_char_indices(target_char):
    indices = []
    for i, char in enumerate(sel_word):
        if char == target_char:
            indices.append(i)
    
    return indices

def win_message():
    clear()
    print("The word is", sel_word)
    print("Congrats on finding the word!")
    exit()

def lose_message():
    clear()
    print("The word was", sel_word)
    print("You lost!")
    exit()

while game_state != sel_word:
    if curr_player + 1 > player_count:
        curr_player = 1
    else:
        curr_player += 1

    if mistake_count == GAME_MAX_MISTAKES:
        lose_message()

    turn()

win_message()