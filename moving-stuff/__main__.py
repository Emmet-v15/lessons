## base window

"""
    read making-a-window if you don't understand something here.
"""

import pygame

pygame.init()

screen = pygame.display.set_mode([512, 512])
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # you can use this to check if a key has just been pressed, and a seperate event when it is released
        # These will be "pygame.KEYDOWN" and "pygame.KEYUP" but we don't want this because it only runs for one frame once you press the key.
        # you can try making a seperate variable to store this but we don't need to.

    
    # a better approach to continous movement while a key is held down, and not having to spam it to move is the following:
    keys = pygame.key.get_pressed()  # get all the keys that are pressed on that single frame.
    if keys[pygame.K_w]: # if the key is the move the shape up: 
        # TODO: move shape
    if keys[pygame.K_DOWN]: # if it is s, then move the shape down:
        # TODO: move shape

    screen.fill((18, 18, 18))
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    pygame.display.flip()

pygame.quit()
