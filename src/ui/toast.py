import pygame


class ToastMessage:
    def __init__(self, screen, message, duration=3, final_y=100):
        self.screen = screen
        self.message = message
        self.duration = duration
        self.final_y = final_y
        self.start_y = screen.get_height()
        self.current_y = self.start_y
        self.start_time = pygame.time.get_ticks()
        self.font = pygame.font.Font(None, 36)
        self.active = True

    def update(self):
        """Update the position of the toast message."""
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - self.start_time) / 1000

        if elapsed_time > self.duration:
            # Calculate the new position of y
            self.current_y += (self.final_y - self.start_y) / 10
        else:
            self.current_y = self.start_y
            self.active = False

    def draw(self):
        """Draw the toast message on the screen."""
        if self.active:
            text_surface = self.font.render(self.message, True, BLACK)
            text_rect = text_surface.get_rect(
                center=(self.screen.get_width() // 2, self.current_y))
            pygame.draw.rect(self.screen, GREY, text_rect.inflate(20, 20))
            self.screen.blit(text_surface, text_rect)
