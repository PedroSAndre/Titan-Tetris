#####################################################main.py############################################################
##Encoding: UTF-8
##End-of-Line Sequence: CRLF

##Main file of the game
##Contains main loop and makes all the references to the main class game

##Authors:

##Pedro Silva André
##José Alberto Cavaleiro Henriques
########################################################################################################################

#Modules Import
import pygame

#Import from other project scripts
from game import game

#Starting program procedures
tetris = game()

#Reading config
tetris.get_config()

#Starting pygame
tetris.start()

last_drop = pygame.time.get_ticks() #Sets the clock
while tetris.running:
    if tetris.new_piece:
        tetris.update_score()
        tetris.insert_piece()
        tetris.new_piece = False
        if(tetris.running == False):
            break

    tetris.draw_board() #Draws everything needed on the screen
        
    for event in pygame.event.get(): #All the events of the game
        if event.type == pygame.QUIT:
            tetris.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                tetris.move_piece(-1,0)
            elif event.key == pygame.K_RIGHT:
                tetris.move_piece(1,0)
            elif event.key == pygame.K_SPACE:
                tetris.rotate_piece()
            elif event.key == pygame.K_DOWN:
                tetris.move_down() #Checks to see if there is a colision and a new piece needs to be introduced
                last_drop=pygame.time.get_ticks()
        
    if((pygame.time.get_ticks()-last_drop)>tetris.interval):
        tetris.move_down() #Checks to see if there is a colision and a new piece needs to be introduced
        last_drop=pygame.time.get_ticks()

tetris.write_results() #Writes results
del tetris