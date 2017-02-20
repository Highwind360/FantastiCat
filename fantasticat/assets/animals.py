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
        self.base_damage = 2
        self.base_defense = 0

    def is_dead(self):
        """Returns whether the animal has died."""
        return self.health == 0

    def move(self, context):
        """The AI will make a decision on behalf of the animal."""
        # TODO: add some AI
        pass

    def hurt(self, amount):
        """Removes a specified amount of health from animal."""
        self.health -= amount
        if self.health <= 0:
            self.alive = False
            self.health = 0

    def attack(self, target):
        "Finds a target to strike, then returns the amount of damage done.
        The returned damage can be zero if the target has too much defense,
        or a negative number in the case of a miss."""
        # TODO: factor in player attack, level, precision, target agility, and stuff like that.
        return self.base_damage - target.base_defense

    def heal(self, amount):
        """Restores the specified amount of health to the animal."""
        print(self.name + " heals " + amount + " HP!")
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


class Cat(Animal):
    default_name = "Cat"

    def scratch(self, target):
        """Basic cat attack. Stings."""
        # TODO: add critical strikes
        #print("You claw violently! Your target recoils.")
        print(self.name + " claws at " + target.name)
        return super().attack(target)

    def heal(self, amount):
        """Restores the specified amount of health to the animal."""
        print(self.name + " cleans its fur.")
        # TODO: critical heal
        #print(self.name + " cleans itself thoroughly, coughs up a hairball")
        super().heal(amount)

    def take_action(self, context):
        """Requires a player to make a decision on what move to make next.
        Performs the requested action."""
        # TODO: do this
        pass


class AnimalNotFoundException():
    """Error that occurs when a nonexistent animal is searched for."""
