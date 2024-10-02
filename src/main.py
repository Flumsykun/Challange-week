import pygame 
from game import Game

def main():
    #Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("BitLife Demo")
    clock = pygame.time.Clock()
    game = Game(screen)
    
    #Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
                game.update() #Update game state
                game.render() #Render game state
                
                #Update display
                pygame.display.flip()
                clock.tick(60)
                
    pygame.quit()
    
    if__name__ == "__main__":
    main()