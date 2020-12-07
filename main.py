#Main file of the game
#Modules Import
import pygame

#Import from other project scriptss
from file_handling import config

#Starting program procedures
config = config()
pygame.init()
screen = pygame.display.set_mode([config.window_width, config.window_height])

running = True

while running:


    # Did the user click the window close button?

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False



pygame.quit()