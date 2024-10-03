import pygame
from player import Player
from events import EventManager
from events import LifeEventManager
from ui.ui import GameUI, StartMenuUI
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE, GREY, BLACK
from ui.toast import ToastMessage
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
        self.showing_game_ui = False
        self.toast_message = None

        # Initialize UI components
        self.start_menu = StartMenuUI()
        self.player = None
        self.ui = None

    def random_event_trigger(self):
        """Trigger a random event based on probability."""
        print("Checking for random event...")  # Debug print
        if random.randint(1, 5) == 1:  # 1 in 5 chance for a life event each year
            event = LifeEventManager.get_random_life_event()
            print(f"Random event triggered: {event['event']}")  # Debug print

            # Apply event impact on player stats
            for stat, value in event["impact"].items():
                if hasattr(self.player, stat):
                    setattr(self.player, stat, getattr(
                        self.player, stat) + value)
                    print(f"Updated {stat} by {value}")  # Debug print
                else:
                    print(f"Player has no attribute {stat}")  # Debug print

            # Create a toast message
            self.toast_message = ToastMessage(self.screen, event["event"])

    def run_year(self):
        """Simulate one year of the game."""
        print("Running a year...")  # Debug print
        self.player.age_up()
        print(f"Player aged up to {self.player.age}")  # Debug print

        # Check if a random event should occur
        self.random_event_trigger()

    def create_random_life(self):
        """Generates random life for the player."""
        names = ['John', 'Jane', 'Alex', 'Emily', 'Chris', 'Katie']
        nationalities = ['American', 'Canadian',
                         'British', 'Dutch', 'German', 'Japanese']
        genders = ['Male', 'Female']

        name = random.choice(names)
        nationality = random.choice(nationalities)
        gender = random.choice(genders)

        # Create the player with random values
        self.player = Player(name, nationality, gender)
        self.ui = GameUI(self.player, self.events)
        self.events.add_event(
            f"You were born as {self.player.name}, a {self.player.gender} from {self.player.nationality}.")
        self.showing_game_ui = True  # Set the flag to show the game UI

    def run(self):
        """Main game loop."""
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP:  # Change to MOUSEBUTTONUP
                    if event.button == 1:  # Left mouse button
                        mouse_pos = pygame.mouse.get_pos()
                        if self.showing_menu:
                            random_button_rect = self.start_menu.update()
                            mouse_pos = pygame.mouse.get_pos()  # Get the mouse position
                            if random_button_rect.collidepoint(mouse_pos):
                                self.create_random_life()
                                self.showing_menu = False
                                print("Random Life selected!")  # Debug message
                        elif self.showing_game_ui and self.player:
                            age_button_rect = self.ui.update()
                            if age_button_rect.collidepoint(pygame.mouse.get_pos()) and not age_button_clicked:
                                self.run_year()  # Increment age by one year
                                self.events.add_event(
                                    f"You are now {self.player.age} years old.")
                                age_button_clicked = True  # Set the flag to true to prevent rapid aging

                if event.type == pygame.MOUSEBUTTONUP:  # Reset the flag when the mouse button is released
                    age_button_clicked = False

            if self.showing_menu:
                self.start_menu.update()
            elif self.showing_game_ui and self.player:
                # Run the main game after player is created
                age_button_rect = self.ui.update()

                if pygame.mouse.get_pressed()[0] and age_button_rect.collidepoint(pygame.mouse.get_pos()):
                    # If the age button is clicked, trigger the year function
                    if not age_button_clicked:
                        self.run_year()  # Call run_year instead of just aging up
                        self.events.add_event(
                            f"You are now {self.player.age} years old.")
                        age_button_clicked = True  # Set the flag to prevent multiple triggers

            if self.toast_message:
                self.toast_message.update()
                self.toast_message.draw()
                if not self.toast_message.active:
                    self.toast_message = None

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()


if __name__ == "__main__":
    game_instance = Game()
    game_instance.run()
