import pygame
from player import Player  # Import the Player class from the player module
from ui import UI  # Import the UI class from the ui module


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

        # Move the player upwards when 'W' is pressed
        if keys[pygame.K_w]:
            # Move up (negative y) at a speed of 300 units/second
            self.player.move(0, -300 * dt)

        # Move the player downwards when 'S' is pressed
        if keys[pygame.K_s]:
            # Move down (positive y) at a speed of 300 units/second
            self.player.move(0, 300 * dt)

        # Move the player left when 'A' is pressed
        if keys[pygame.K_a]:
            # Move left (negative x) at a speed of 300 units/second
            self.player.move(-300 * dt, 0)

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
