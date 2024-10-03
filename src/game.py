import pygame
from player import Player
from events import EventManager
from events import LifeEventManager
from ui import GameUI, StartMenuUI
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE, GREY, BLACK
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
        self.showing_game_ui = False

        # Initialize UI components
        self.start_menu = StartMenuUI()
        self.player = None
        self.ui = None

    # Defines the random event trigger method
    def random_event_trigger(self):
        """Trigger a random event based on probability."""
        if random.randint(1, 5) == 1:  # 1 in 5 chance for a life event each year
            event = LifeEventManager.get_random_life_event()
            print(event["event"])

            # Apply event impact on player stats
            for stat, value in event["impact"].items():
                setattr(self.player, stat, getattr(self.player, stat) + value)

    def run_year(self):
        """Simulate one year of the game."""
        self.player.age_up()

        # Check if a random event should occur
        self.random_event_trigger()

        # Dropdown for nationality
        self.selected_nationality = 'American'
        self.nationality_options = ['American', 'Canadian', 'British', 'Dutch', 'German', 'Japanese']

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
        self.events.add_event(f"You were born as {self.player.name}, a {self.player.gender} from {self.player.nationality}.")
        self.showing_game_ui = True  # Set the flag to show the game UI

    def custom_life_input(self):
        """Handles custom life input from the user."""
        input_box_name = pygame.Rect(300, 200, 140, 32)
        input_box_gender = pygame.Rect(300, 300, 140, 32)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color_name = color_inactive
        color_gender = color_inactive
        text_name = ''
        text_gender = ''
        active_name = False
        active_gender = False

        # Begin de invoerloop
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box_name.collidepoint(event.pos):
                        active_name = not active_name
                    else:
                        active_name = False
                    color_name = color_active if active_name else color_inactive

                    if input_box_gender.collidepoint(event.pos):
                        active_gender = not active_gender
                    else:
                        active_gender = False
                    color_gender = color_active if active_gender else color_inactive

                if event.type == pygame.KEYDOWN:
                    if active_name:
                        if event.key == pygame.K_RETURN:
                            active_name = False
                        elif event.key == pygame.K_BACKSPACE:
                            text_name = text_name[:-1]
                        else:
                            text_name += event.unicode
                    if active_gender:
                        if event.key == pygame.K_RETURN:
                            active_gender = False
                        elif event.key == pygame.K_BACKSPACE:
                            text_gender = text_gender[:-1]
                        else:
                            text_gender += event.unicode

            self.screen.fill(WHITE)

            # Render naam invoerveld
            self.draw_text("Enter Name:", 250, 170)
            txt_surface_name = pygame.font.Font(None, 32).render(text_name, True, color_name)
            width = max(200, txt_surface_name.get_width() + 10)
            input_box_name.w = width
            self.screen.blit(txt_surface_name, (input_box_name.x + 5, input_box_name.y + 5))
            pygame.draw.rect(self.screen, color_name, input_box_name, 2)

            # Render geslacht invoerveld
            self.draw_text("Enter Gender (Male/Female):", 150, 270)
            txt_surface_gender = pygame.font.Font(None, 32).render(text_gender, True, color_gender)
            width = max(200, txt_surface_gender.get_width() + 10)
            input_box_gender.w = width
            self.screen.blit(txt_surface_gender, (input_box_gender.x + 5, input_box_gender.y + 5))
            pygame.draw.rect(self.screen, color_gender, input_box_gender, 2)

            # Dropdown voor nationaliteit
            dropdown_rect = pygame.Rect(300, 400, 140, 32)
            pygame.draw.rect(self.screen, GREY, dropdown_rect)
            dropdown_surface = pygame.font.Font(None, 32).render(self.selected_nationality, True, BLACK)
            self.screen.blit(dropdown_surface, (dropdown_rect.x + 5, dropdown_rect.y + 5))

            if pygame.mouse.get_pressed()[0]:
                if dropdown_rect.collidepoint(pygame.mouse.get_pos()):
                    # Toggle dropdown selectie
                    current_index = self.nationality_options.index(self.selected_nationality)
                    self.selected_nationality = self.nationality_options[(current_index + 1) % len(self.nationality_options)]

            # Render nationaliteit keuze
            self.draw_text("Select Nationality:", 250, 370)

            # Render de startknop
            start_button_rect = pygame.Rect(300, 500, 140, 32)  # Definieer een rechthoek voor de startknop
            pygame.draw.rect(self.screen, color_active if (text_name and text_gender) else color_inactive, start_button_rect)
            self.draw_text("Start Game", 315, 505)  # Plaats de tekst in de knop

            # Controleer of de startknop is ingedrukt
            if pygame.mouse.get_pressed()[0] and start_button_rect.collidepoint(pygame.mouse.get_pos()):
                if text_name and text_gender:  # Zorg ervoor dat beide velden zijn ingevuld
                    self.player = Player(text_name, self.selected_nationality, text_gender)
                    self.ui = GameUI(self.player, self.events)
                    self.events.add_event(f"You were born as {self.player.name}, a {self.player.gender} from {self.player.nationality}.")
                    self.showing_game_ui = True  # Switch to the main game UI after custom life input
                    done = True  # Exit the input loop

            pygame.display.flip()
            self.clock.tick(FPS)

    def draw_text(self, text, x, y):
        """Draws text on the screen."""
        font = pygame.font.Font(None, 32)
        text_surface = font.render(text, True, BLACK)
        self.screen.blit(text_surface, (x, y))

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
                            mouse_pos = pygame.mouse.get_pos()  # Get the mouse position
                            if custom_button_rect.collidepoint(mouse_pos):
                                self.showing_custom_life = True
                                self.showing_menu = False
                                print("Custom Life selected!")  # Debug message
                                self.custom_life_input()  # Call the input method
                            elif random_button_rect.collidepoint(mouse_pos):
                                self.create_random_life()
                                self.showing_menu = False
                                print("Random Life selected!")  # Debug message

            if self.showing_menu:
                # Show start menu
                self.start_menu.update()
            elif self.showing_custom_life:
                # No longer loop infinitely, as input is handled in custom_life_input
                print("In Custom Life setup...")  # Debug message
            elif self.showing_game_ui and self.player:
                # Run the main game after player is created
                age_button_rect = self.ui.update()

                if pygame.mouse.get_pressed()[0] and age_button_rect.collidepoint(pygame.mouse.get_pos()):
                    self.player.age_up()
                    self.events.add_event(
                        f"You are now {self.player.age} years old.")

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == "__main__":
    game_instance = Game()
    game_instance.run()













