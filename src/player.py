import pygame


class Player:
    def __init__(self):
        self.position = pygame.Vector2(400, 300)
        self.image = pygame.Surface((50, 50))  # Create a simple square player
        self.image.fill("blue")  # Fill the square with blue color

        self.stats = {
            "health": 100,
            "money": 1000,
            "happiness": 80
        }

    def move(self, dx, dy):
        self.position.x += dx
        self.position.y += dy

    def render(self, screen):
        screen.blit(self.image, self.position)
