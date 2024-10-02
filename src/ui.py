# ui.py
import pygame
from config import WHITE, BLACK, GREY, FONT
from config import SCREEN_WIDTH, SCREEN_HEIGHT


class GameUI:
    """Handles the user interface for the game."""

    def __init__(self, player, event_manager):
        self.player = player
        self.events = event_manager

    def draw_text(self, text, x, y):
        """Draws text on the screen."""
        screen = pygame.display.get_surface()
        text_surface = FONT.render(text, True, BLACK)
        screen.blit(text_surface, (x, y))

    def draw_button(self, text, x, y, width, height, color=GREY):
        """Draws a button on the screen."""
        screen = pygame.display.get_surface()
        button_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, color, button_rect)
        text_surface = FONT.render(text, True, BLACK)
        screen.blit(text_surface, (x + (width // 2 - text_surface.get_width() //
                    2), y + (height // 2 - text_surface.get_height() // 2)))
        return button_rect

    def update(self):
        """Updates the UI, including player stats and event log."""
        screen = pygame.display.get_surface()
        screen.fill(WHITE)

        # Draw player stats
        self.draw_text(f"Age: {self.player.age}", 50, 50)
        self.draw_text(f"Happiness: {self.player.happiness}", 50, 100)
        self.draw_text(f"Health: {self.player.health}", 50, 150)
        self.draw_text(f"Smarts: {self.player.smarts}", 50, 200)
        self.draw_text(f"Looks: {self.player.looks}", 50, 250)

        # Draw event log
        pygame.draw.rect(screen, GREY, (400, 50, 350, 400))
        self.draw_text("Event Log:", 410, 60)

        # Show recent events
        recent_events = self.events.get_recent_events()
        for i, event in enumerate(recent_events):
            self.draw_text(event, 410, 100 + i * 30)

        # Draw buttons
        age_button = self.draw_button('Age Up', 50, 400, 150, 50)

        # Handle button events, moved the logic to game.py
        return age_button


class StartMenuUI:
    """Handles the start menu where the player chooses Custom Life or Random Life."""

    def update(self):
        """Updates the start menu."""
        screen = pygame.display.get_surface()
        screen.fill(WHITE)

        # Draw title
        title_font = pygame.font.SysFont('Arial', 40)
        title_surface = title_font.render("Welcome to BitLife", True, BLACK)
        screen.blit(title_surface, (SCREEN_WIDTH // 2 -
                    title_surface.get_width() // 2, 100))

        # Draw Custom Life button
        custom_button_rect = self.draw_button('Custom Life', 300, 300, 200, 50)

        # Draw Random Life button
        random_button_rect = self.draw_button('Random Life', 300, 400, 200, 50)

        return custom_button_rect, random_button_rect

    def draw_button(self, text, x, y, width, height, color=GREY):
        """Draws a button on the screen."""
        screen = pygame.display.get_surface()
        button_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, color, button_rect)
        text_surface = FONT.render(text, True, BLACK)
        screen.blit(text_surface, (x + (width // 2 - text_surface.get_width() //
                    2), y + (height // 2 - text_surface.get_height() // 2)))
        return button_rect
