import pygame


class ToastMessage:
    def __init__(self, screen, message, duration=3, final_y=100):
        self.screen = screen
        self.message = message
        self.duration = duration  # Duration the toast stays on screen
        self.final_y = final_y  # Final position where the toast will stop
        self.start_y = screen.get_height()  # Start off-screen
        self.current_y = self.start_y
        self.start_time = pygame.time.get_ticks()
        self.font = pygame.font.Font(None, 36)
        self.active = True  # Keep toast active until it's finished

    def update(self):
        """Update the position of the toast message."""
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - self.start_time) / \
            1000  # Seconds passed

        if elapsed_time < self.duration:  # If the toast hasn't reached the duration
            # Animate the movement towards the final_y position
            move_speed = (self.start_y - self.final_y) / \
                20  # Smooth the animation
            self.current_y = max(self.final_y, self.current_y - move_speed)
        else:
            # After duration, start moving the toast off-screen
            self.current_y += 5  # Speed at which the toast moves off the screen
            if self.current_y > self.screen.get_height():  # If off-screen
                self.active = False  # Deactivate the toast

    def draw(self):
        """Draw the toast message on the screen."""
        if self.active:
            # Render the text
            text_surface = self.font.render(self.message, True, (0, 0, 0))
            text_rect = text_surface.get_rect(
                center=(self.screen.get_width() // 2, self.current_y))

            # Draw a background rectangle for the toast message
            pygame.draw.rect(self.screen, (128, 128, 128),
                             text_rect.inflate(20, 20))
            self.screen.blit(text_surface, text_rect)
