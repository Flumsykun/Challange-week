#main program

import pygame

#pygame setup
pygame.init()
screen = pygame.display.set_module((1280, 70))
clock = pygame.time.clock()
running = True

while running:
    #poll for events
    #pygame.QUIT events means the user click on X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    #RENDER YOUR GAME HERE

    #flip() the display to put the work on screen
    pygame.display.flip()

    clock.tick(60) #limits FPS to 60

pygame.quit()            