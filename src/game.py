# game.py
import pygame
from player import Player
from events import EventManager
from ui import GameUI, StartMenuUI
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS  # <-- Import screen settings
import random

class Game:
    """Main game class, manages player, events, and game loop."""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("BitLife")
        self.clock = pygame.time.Clock()

        self.events = EventManager()

        # Initial state: show start menu
        self.showing_menu = True
        self.showing_custom_life = False

        # Initialize UI components
        self.start_menu = StartMenuUI()

        self.player = None
        self.ui = None

    def create_random_life(self):
        """Generates random life for the player."""
        names = ['John', 'Jane', 'Alex', 'Emily', 'Chris', 'Katie']
        nationalities = ['American', 'Canadian', 'British', 'Dutch', 'German', 'Japanese']
        genders = ['Male', 'Female']

        name = random.choice(names)
        nationality = random.choice(nationalities)
        gender = random.choice(genders)

        # Create the player with random values
        self.player = Player(name, nationality, gender)
        self.ui = GameUI(self.player, self.events)
        self.events.add_event(f"You were born as {self.player.name}, a {self.player.gender} from {self.player.nationality}.")
    
    def run(self):
        """Main game loop."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        if self.showing_menu:
                            custom_button_rect, random_button_rect = self.start_menu.update()
                            if custom_button_rect.collidepoint(pygame.mouse.get_pos()):
                                self.showing_custom_life = True
                                self.showing_menu = False
                            elif random_button_rect.collidepoint(pygame.mouse.get_pos()):
                                self.create_random_life()
                                self.showing_menu = False

            if self.showing_menu:
                # Show start menu
                self.start_menu.update()
            elif self.showing_custom_life:
                # Custom life logic (to be implemented in the next step)
                pass
            elif self.player:
                # Run the main game after player is created
                age_button_rect = self.ui.update()

                if pygame.mouse.get_pressed()[0] and age_button_rect.collidepoint(pygame.mouse.get_pos()):
                    self.player.age_up()
                    self.events.add_event(f"You are now {self.player.age} years old.")

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()



