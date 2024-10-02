# game.py
import pygame
from player import Player
from events import EventManager
from ui import GameUI
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

class Game:
    """Main game class, manages player, events, and game loop."""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("BitLife")
        self.clock = pygame.time.Clock()

        # Initialize player, events, and UI
        self.player = Player("Player 1")
        self.events = EventManager()
        self.ui = GameUI(self.player, self.events)

        # Start with a birth event
        self.events.add_event("You were born!")
    
    def run(self):
        """Main game loop."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Update the game state
            self.ui.update()

            # Refresh screen
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
