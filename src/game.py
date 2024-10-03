import pygame
<<<<<<< Updated upstream
from player import Player  # Import the Player class from the player module
from ui import UI  # Import the UI class from the ui module
=======
from player import Player
from events import EventManager
from events import LifeEventManager
from activities.activities import get_activities_for_age
from ui.ui import GameUI, StartMenuUI
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE, GREY, BLACK
from ui.toast import ToastMessage
import random
>>>>>>> Stashed changes


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

<<<<<<< Updated upstream
        # Move the player upwards when 'W' is pressed
        if keys[pygame.K_w]:
            # Move up (negative y) at a speed of 300 units/second
            self.player.move(0, -300 * dt)
=======
        self.player = Player
        self.available_activities = get_activities_for_age(self.player.age)

        # Initial state: show start menu
        self.showing_menu = True
        self.showing_game_ui = False
        self.toast_message = None
>>>>>>> Stashed changes

        # Move the player downwards when 'S' is pressed
        if keys[pygame.K_s]:
            # Move down (positive y) at a speed of 300 units/second
            self.player.move(0, 300 * dt)

<<<<<<< Updated upstream
        # Move the player left when 'A' is pressed
        if keys[pygame.K_a]:
            # Move left (negative x) at a speed of 300 units/second
            self.player.move(-300 * dt, 0)
=======
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
>>>>>>> Stashed changes

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
        # Main game loop
        clock = pygame.time.Clock()  # Create a clock object to manage time
        running = True  # Game loop control variable

        while running:
            # Limit the frame rate to 60 FPS and calculate delta time in seconds
            dt = clock.tick(60) / 1000
            running = self.handle_events()  # Check for events like quitting
            self.update(dt)  # Update the game state (player movement, etc.)
            self.render()  # Render everything on the screen
            pygame.display.flip()  # Update the display with everything rendered


# Initialize Pygame and set up the game window
pygame.init()  # Initialize all Pygame modules

# Set up the screen with a resolution of 800x600 pixels
screen = pygame.display.set_mode((800, 600))

# Create a game instance and run the game
game = Game(screen)  # Create a Game object, passing in the screen
game.run()  # Start the game loop

# Quit Pygame when the game loop ends
pygame.quit()
