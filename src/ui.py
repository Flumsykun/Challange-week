# User interface handling
import pygame


class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font("assets/fonts/AvenirLTStd-Light.ttf", 36)

    def draw_text(self, text, position, color=(255, 255, 255)):
        """Render text at the given position."""
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, position)

    def draw_stats(self, player_stats):
        """Draw player stats like health, money, happiness."""
        health_text = f"Health: {player_stats['health']}"
        money_text = f"Money: {player_stats['money']}"
        happiness_text = f"Happiness: {player_stats['happiness']}"

        # Draw stats on the screen
        self.draw_text(health_text, (20, 20))
        self.draw_text(money_text, (20, 60))
        self.draw_text(happiness_text, (20, 100))
