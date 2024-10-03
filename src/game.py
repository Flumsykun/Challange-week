import pygame
from player import Player
from events import EventManager
from events import LifeEventManager
from activities.activities import get_activities_for_age
from ui.ui import GameUI, StartMenuUI
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE, GREY, BLACK
from ui.toast import ToastMessage
import random


class Game:
    def __init__(self, screen):
        # Initialize the game with the provided screen and a player instance
        # The Pygame screen object where the game is rendered
        self.screen = screen
        self.player = Player()  # Create a player object
        self.ui = UI(screen)  # Create a UI object for displaying text

    def handle_events(self):
        # Handle all Pygame events (like key presses, window close, etc.)
        for event in pygame.event.get():  # Get all events that have occurred
            if event.type == pygame.QUIT:  # If the user closes the window
                return False  # Stop the game loop
        return True  # Continue running the game loop if no quit event

    def update(self, dt):
        # Update game objects, specifically the player's position based on input
        # dt (delta time) is the time passed since the last frame for
        # frame-independent movement
        keys = pygame.key.get_pressed()  # Get the state of all keys (pressed or not)

        self.player = Player
        self.available_activities = get_activities_for_age(self.player.age)

        # Initial state: show start menu
        self.showing_menu = True
        self.showing_game_ui = False
        self.toast_message = None

        # Move the player downwards when 'S' is pressed
        if keys[pygame.K_s]:
            # Move down (positive y) at a speed of 300 units/second
            self.player.move(0, 300 * dt)

    def update(self):
        # Update game logic, including player stats and events
        for activity in self.available_activities:
            activity.check_availabilty(self.player.age)
            print(f"Activity {activity.name} available: {activity.available}")

    def random_event_trigger(self):
        """Trigger a random event based on probability."""
        print("Checking for random event...")  # Debug print
        if random.randint(1, 5) == 1:  # 1 in 5 chance for a life event each year
            event = LifeEventManager.get_random_life_event()
            print(f"Random event triggered: {event['event']}")  # Debug print

        # Move the player right when 'D' is pressed
        if keys[pygame.K_d]:
            # Move right (positive x) at a speed of 300 units/second
            self.player.move(300 * dt, 0)

    def render(self):
        # Render all game objects onto the screen
        self.screen.fill((50, 50, 50))
        self.player.render(self.screen)
        # Render the player's stats on the screen
        self.ui.draw_stats(self.player.stats)

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
