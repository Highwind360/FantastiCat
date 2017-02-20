#!/usr/bin/env python3
"""
game.py
Grayson Sinclair

Begins a game of fantasticats for the user.
"""

import os
import json
from assets import animals

BASE_DIR = os.path.dirname(__file__)
LEVEL_FILE = '/data/level_data.json'
LEVEL_DATA = json.load(open(BASE_DIR + LEVEL_FILE, 'r'))


def attempt_level(level_no):
    """Plays the specified level.
    Returns True in the case of victory, False elsewise."""
    level = LEVEL_DATA[level_no]
    dramatic_print("Level {num}: {name}".format(num=level_no,
                   name=level["name"]), 120)
    print(level["intro"])

    player = animals.Cat()
    enemies = []
    for spawn in level["enemies"]:
        if spawn["type"] == "Dog":
            enemy = animals.Dog()
        else:
            raise animals.AnimalNotFoundException(
                "An improper animal is defined in the level data. " +
                "Check {lvl_dat} for more info.".format(lvl_dat=LEVEL_FILE)
            )
        enemies.append(enemy)

    while len(enemies) > 0:
        if player.is_dead():
            print("You were struck down.")
            return False
        else:
            player.take_action()
        for enemy in enemies:
            if enemy.is_dead():
                enemies.remove(enemy)
            else:
                enemy.move(player)
        if len(enemies) == 0:
            return True

def welcome_prompt():
    """Prompts the user with the game opening banner.
    If the player chooses to begin, the method returns True. Any other input
    will return False."""
    print("Welcome, Traveler.")
    print("As you will discover very soon, you are a cat.")
    print("There are many trials before you.")
    answer = input("Feeling curious? [Y/N]: ").upper()
    while len(answer) == 0 or answer[0] not in ['Y', 'N']:
        print("Taking a nap on the keyboard, are you?")
        answer = input("Please enter either [Y]es or [N]o: ").upper()

    if answer[0] == 'Y':
        print("Good luck.")
        return True
    else:
        print("Ah. Maybe another day, then.")
        print("After all, Destiny does not beckon every kitten that meows.")
        print("Come back when you're older and more curious.")
        return False

def dramatic_print(mesg, timing=50, delay=150):
    """A wrapper for print.
    Will print out the mesg entered with the timing specified.
    It will then wait for the specified delay before continuing."""
    # TODO: Finish the implementation of this!
    print(mesg)

def play(starting_level = 1, starting_lives = 9):
    lives = starting_lives
    level_no = starting_level - 1

    playing = welcome_prompt()
    while playing:
        choice = input(
            "You have {num} lives. Are you curious? [Y/n]: ".format(num=lives)
        )
        if len(choice) > 0 and choice[0].upper() == 'N':
            print("You are suddenly overcome by a chilling fear. " +
                  "You decide to stay home.")
            dramatic_print("For the rest of your life.", 200)
            break

        did_succeed = attempt_level(level_no)
        if did_succeed:
            level += 1
        else:
            lives -= 1

        playing = lives > 0
        if not playing:
            print("You have died. I suppose curiosity really does kill.")

def main():
    """Takes the user's command line input,\
    and feeds it to the game's play\ function."""
    print("Starting Game...")
    # TODO: accept startup options and pass them to the game
    while True:
        play()


if __name__ == "__main__":
    main()
