# import zone
import pygame
# initialize pygame
pygame.init()
# create a screen
screen = pygame.display.set_mode([800,600],pygame.RESIZABLE)
# fill with color WHITE
screen.fill([255,255,255])
# load and show the image of lanbo
jpgFileName = 'lanbo800_600.jpg'
imgRect = pygame.image.load(jpgFileName)
screen.blit(imgRect,[0,0])
# load and show the sound of firstblood
wavFileName = 'FirstBlood.wav'
sndTrack = pygame.mixer.music.load(wavFileName)
pygame.mixer.music.play()
# flip
pygame.display.flip()
# LOOP: mRunning
mRunning = True
while mRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mRunning = False
            pygame.quit()
    pygame.display.flip()        
