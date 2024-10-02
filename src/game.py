# Core game logic
# Import the Player class
from player import Player


# Game class
class Game:
    # Constructor
    def __init__(self, screen):
        # Initialize game
        self.screen = screen
        self.player = Player()

    def update(self):
        # Update the player's stats or handle events
        self.player.update()

    def render(self):
        # Fill the screen with a background color
        self.screen.fill((50, 50, 50))
        self.player.render(self.screen)
