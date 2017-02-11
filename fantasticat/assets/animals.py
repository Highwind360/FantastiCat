"""
animals.py
Grayson Sinclair
Justin Collins

Declares the animals that will be present in fantasticat.
"""


class Animal():
    """The base class for an animal."""
    default_name = "Animal"

    def __init__(self, name = default_name, max_health = 3):
        self.max_health = max_health
        self.health = max_health
        self.name = name
        self.alive = True

    def hurt(self, amount):
        """Removes a specified amount of health from animal."""
        self.health -= amount
        if self.health <= 0:
            self.alive = False
            self.health = 0

    def heal(self, amount):
        """Restores the specified amount of health to the animal."""
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health


class Dog(Animal):
    """An ordinary dog. Can bark and bite. Inherits animal."""
    default_name = "Dog"

    def bark(self):
        print("The dog barks!")

    def bite(self):
        print("The dog bites!")
