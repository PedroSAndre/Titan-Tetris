#Main file of the game
#Modules Import
import pygame

#Import from other project scriptss
from game import game

#Starting program procedures
tetris = game()

#Reading config
tetris.get_config()

#Starting pygame
tetris.start()

while tetris.running:
    tetris.draw_board()
    pygame.time.wait(1000)
    for event in pygame.event.get():
        #If the user wants to exit
        if event.type == pygame.QUIT:
            tetris.running = False


del tetris
pygame.quit()