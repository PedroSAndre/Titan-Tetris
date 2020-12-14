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

last_drop = pygame.time.get_ticks() #Sets the clock
while tetris.running:
    if tetris.new_piece:
        tetris.update_score()
        tetris.insert_piece()
        tetris.new_piece = False

    tetris.draw_board()
        
    for event in pygame.event.get():
        #If the user wants to exit
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
                tetris.move_down() #Checks to see if there is a colision
                last_drop=pygame.time.get_ticks()
        
    if((pygame.time.get_ticks()-last_drop)>tetris.interval):
        tetris.move_down() #Checks to see if there is a colision
        last_drop=pygame.time.get_ticks()


del tetris
pygame.quit()