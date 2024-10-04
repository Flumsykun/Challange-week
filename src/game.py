import pygame
from player import Player
from events import EventManager
from activities.activities import get_activities_for_age
from ui.ui import GameUI, StartMenuUI
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE, GREY, BLACK
from ui.toast import ToastMessage
import random


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player()  # Create a player object
        # Game UI for the stats and activities
        self.ui = GameUI(self.player, EventManager())
        self.start_menu = StartMenuUI()  # Start menu UI for Random Life
        self.showing_menu = True  # Show start menu initially
        self.showing_activities = False  # Activities hidden at the start
        self.available_activities = get_activities_for_age(self.player.age)
        self.toast_message = None

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if self.showing_menu:
                    random_button_rect = self.start_menu.update()
                    if random_button_rect.collidepoint(mouse_pos):
                        self.create_random_life()
                        self.showing_menu = False  # Exit start menu
                        print("Random Life selected!")
                else:
                    if self.ui.hamburger_menu_rect.collidepoint(mouse_pos):
                        self.showing_activities = not self.showing_activities  # Toggle activities

                    # Handle activity selection if the activity menu is open
                    if self.showing_activities:
                        activity_rects = self.ui.get_activity_rects(
                            self.available_activities)
                        for i, rect in enumerate(activity_rects):
                            if rect.collidepoint(mouse_pos):
                                self.handle_activity_selection(
                                    self.available_activities[i])

        return True

    def update(self):
        """Update game logic, including activities and stats."""
        if not self.showing_menu and not self.showing_activities:
            for activity in self.available_activities:
                activity.check_availabilty(self.player.age)

    def render(self):
        self.screen.fill(WHITE)
        if self.showing_menu:
            self.start_menu.update()
        else:
            self.ui.update()
            if self.showing_activities:
                self.ui.draw_activity_menu(self.available_activities)

        if self.toast_message:
            self.toast_message.update()
            self.toast_message.draw()

        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.render()
            clock.tick(FPS)

        pygame.quit()

    def create_random_life(self):
        """Set up a new random life for the player."""
        self.player = Player()
        self.toast_message = ToastMessage(self.screen, "Random Life Created")

    def handle_activity_selection(self, selected_activity):
        """Apply the effects of the selected activity."""
        if selected_activity.available:
            print(
                f"Selected {selected_activity.name}: {selected_activity.description}")
            self.apply_activity_effects(selected_activity)
        else:
            print(f"You are too young for {selected_activity.name}.")

    def apply_activity_effects(self, activity):
        """Modify player's stats based on the selected activity."""
        if activity.name == "Go to Gym":
            self.player.health += 10  # Example
        elif activity.name == "Travel":
            self.player.happiness += 5
        # Add more activity logic here
