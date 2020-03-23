import pygame
from pygame.color import THECOLORS

# initial
pygame.init()

# create a window
screen = pygame.display.set_mode([600, 400])

# fill the window with WHITE
screen.fill(THECOLORS['white'])

# draw the blue part and red part
pygame.draw.rect(screen, THECOLORS['blue'], [0, 0, 200, 400], 0)
pygame.draw.rect(screen, THECOLORS['red'], [400, 0, 200, 400], 0)

# flip
pygame.display.flip()

# main while
mRunning = True
while mRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.image.save(screen, "FranceFlag.jpg")
            mRunning = False
pygame.quit()
