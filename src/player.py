# player.py
class Player:
    """Represents the player with stats like age, happiness, etc."""
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.happiness = 100
        self.health = 100
        self.smarts = 100
        self.looks = 100

    def age_up(self):
        """Increases player's age and adjusts stats."""
        self.age += 1
        self.happiness -= 5
        self.health -= 5
        self.smarts += 2
        self.looks -= 1
