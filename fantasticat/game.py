#!/usr/bin/env python3
"""
game.py
Grayson Sinclair

Begins a game of fantasticats for the user.
"""

from assets import animals


def play():
    print("Generating Dog...")
    d = animals.Dog()
    d.bark()
    d.bite()

def main():
    print("Starting Game...")
    # TODO: accept startup options and pass them to the game
    play()


if __name__ == "__main__":
    main()
