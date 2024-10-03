import pygame
from config import FONT  # Ensure you have FONT defined in your config


class Activity:
    """Class to represent an activity in the game."""

    def __init__(self, name, description, min_age):
        self.name = name
        self.description = description
        self.min_age = min_age
        self.available = False

    def check_availabilty(self, player_age):
        """Check if the activity is available based on player's age."""
        self.available = player_age >= self.min_age


class Player:
    """Class to represent the player in the game."""

    def __init__(self, age):
        self.age = age


class Game:
    """Main game class"""

    def __init__(self):
        self.activities = [
            Activity("Adoption", "Adopt a child", 18),
            Activity("Visit Casino", "Play a minigame of Blackjack.", 18),
            Activity("Go to School",
                     "Enroll in a course to improve your skills.", 6),
            Activity("Go to Gym", "Work out to improve your health.", 8),
            Activity("Travel", "Go on a vacation to a new country.", 3),
            Activity("Start a Business",
                     "Become an entrepreneur and start a business.", 16),
            Activity("Get Married", "Find a partner and get married.", 18),
            Activity("Buy a House", "Purchase a house to live in.", 18),
            Activity("Buy a Car", "Purchase a car to drive around.", 16),
            Activity("Go to Doctor", "Get a checkup from a doctor.", 0),
            Activity("Go to Dentist", "Get a checkup from a dentist.", 1),
            Activity("Go to Therapist",
                     "Get therapy to improve your mental health.", 5),
            Activity("Commit a Crime",
                     "Break the law and face the consequences.", 11),
        ]
        self.player = Player(18)  # Set an initial age for testing

    def update_activities(self):
        """Update the availability of activities based on player's age."""
        for activity in self.activities:
            activity.check_availabilty(self.player.age)

    def display_activities(self):
        """Display the available activities to the player."""
        screen = pygame.display.get_surface()
        for i, activity in enumerate(self.activities):
            color = (200, 200, 200) if not activity.available else (
                255, 255, 255)  # Change color based on availability
            text_surface = FONT.render(activity.name, True, color)
            screen.blit(text_surface, (50, 100 + i * 30))

    def handle_activity_selection(self, selected_activity):
        """Handle what happens when an activity is selected."""
        if selected_activity.available:
            # Trigger the activity (implement the logic for each activity)
            print(
                f"You chose to {selected_activity.name}: {selected_activity.description}")
        else:
            print(f"You are too young to {selected_activity.name}.")


# Initialize Pygame and create game instance
pygame.init()
screen = pygame.display.set_mode((800, 600))
FONT = pygame.font.SysFont('Arial', 24)

game = Game()
game.update_activities()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear the screen
    game.display_activities()

    pygame.display.flip()

pygame.quit()
