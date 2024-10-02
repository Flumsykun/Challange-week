import pygame


class Player:
    # define the player's attributes
    def __init__(self):
        self.position = pygame.Vector2(400, 300)
        self.color = (255, 0, 0)  # Red color for the player
        self.radius = 20

        def update(self):
            # Placeholder: update player's stats or handle events
            pass

        def render(self, screen):
            pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)