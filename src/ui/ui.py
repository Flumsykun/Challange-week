import pygame
from config import WHITE, BLACK, DARK_GREY, FONT


class GameUI:
    def __init__(self, player, event_manager):
        self.player = player
        self.events = event_manager
        self.hamburger_menu_rect = pygame.Rect(
            700, 50, 50, 50)  # Position for hamburger menu

    def draw_text(self, text, x, y):
        screen = pygame.display.get_surface()
        text_surface = FONT.render(text, True, BLACK)
        screen.blit(text_surface, (x, y))

    def draw_button(self, text, x, y, width, height, color=DARK_GREY):
        screen = pygame.display.get_surface()
        button_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, color, button_rect, border_radius=5)
        text_surface = FONT.render(text, True, WHITE)
        screen.blit(text_surface, (x + (width // 2 - text_surface.get_width() // 2),
                                   y + (height // 2 - text_surface.get_height() // 2)))
        return button_rect

    def update(self):
        screen = pygame.display.get_surface()
        screen.fill(WHITE)

        # Draw player stats
        self.draw_text(f"Age: {self.player.age}", 50, 50)
        self.draw_text(f"Happiness: {self.player.happiness}", 50, 100)
        self.draw_text(f"Health: {self.player.health}", 50, 150)
        self.draw_text(f"Smarts: {self.player.smarts}", 50, 200)
        self.draw_text(f"Looks: {self.player.looks}", 50, 250)

        # Draw the hamburger menu button
        pygame.draw.rect(screen, DARK_GREY, self.hamburger_menu_rect)
        self.draw_text("≡", self.hamburger_menu_rect.x +
                       15, self.hamburger_menu_rect.y + 5)

    def draw_activity_menu(self, activities):
        screen = pygame.display.get_surface()
        y_offset = 100
        for activity in activities:
            color = (150, 150, 150) if not activity.available else (0, 0, 0)
            activity_surface = FONT.render(activity.name, True, color)
            screen.blit(activity_surface, (50, y_offset))
            y_offset += 40

    def get_activity_rects(self, activities):
        rects = []
        y_offset = 100
        for activity in activities:
            rect = pygame.Rect(50, y_offset, 200, 30)
            rects.append(rect)
            y_offset += 40
        return rects
