# player.py
from utils import clamp

class Player:
    """Represents the player with stats like age, happiness, health, etc."""
    def __init__(self, name, nationality, gender):
        self.name = name
        self.nationality = nationality
        self.gender = gender
        self.age = 0
        self.happiness = 100
        self.health = 100
        self.smarts = 100
        self.looks = 100

    def age_up(self):
        """Increases player's age and adjusts stats, ensuring they don't go below 0."""
        self.age += 1
        self.happiness = clamp(self.happiness - 5, 0, 100)
        self.health = clamp(self.health - 5, 0, 100)
        self.smarts = clamp(self.smarts + 2, 0, 100)
        self.looks = clamp(self.looks - 1, 0, 100)
