#Class with all the game variables to be used
#The oficial board is 10x20, so this values cannot be changed
import pygame
from piece import piece
from general_functions import check_pair_in_list

class game():
    def __init__(self):
        #All variables necessary for the game
        self.level=1
        self.points=0 
        self.interval=1000 #Interval in seconds between drops
        self.intervaldrop=0.95

        self.points_to_new_level=10000
        self.points_per_line_cleared=1000

        self.window=None #Needs to wait for window to be created in main loop
        self.window_width=None
        self.window_height=None
        self.square_side=None
        self.window_title='Titan Tetris'
        self.icon_path='sources/icon.png'
        self.music='sources/TetrisTheme.mp3'
        self.background_color=[255,255,255] #white background color
        self.grid_color=[169,169,169] #grid lines color

        self.board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]] #Saves the information about all squares on the board
        self.current_piece = None
        self.new_piece = True

        self.running=True #Variable for the main game loop

    #Function to read or create the config file for the game (includes window height and width)
    def get_config(self):
        try:
            file = open('config.txt','r')
            for i in file.readlines():
                i = i.split(':')
                if('Window_width' in i[0]):
                    self.window_width = int(i[1])
        except Exception as e:
            if isinstance(e, ValueError) or isinstance(e, IOError):
                print('It wasn\'t possible to read the config file\nGoing back to default values')
                try:
                    file = open('config.txt','w')
                    file.write('Window_width (px): 300')
                    self.window_width = 300
                except IOError:
                    print('Fatal error creating config file\nPlease verify that you have read and write permissions')
                    exit(0)

    #Fuction to create the playing window
    def start(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.music)
        pygame.init()

        self.square_side = int((self.window_width)/10)
        self.window_height = (21)*(self.square_side)

        self.window = pygame.display.set_mode([self.window_width, self.window_height])
        pygame.display.set_caption(self.window_title)
        pygame.display.set_icon(pygame.image.load(self.icon_path))

        
        pygame.mixer.music.play(-1)


    #Function to draw grid and update the score
    def draw_grid(self):
        for i in range(1, 21):
            for j in range(10):
                pygame.draw.rect(self.window, self.grid_color, pygame.Rect(j*self.square_side, i*self.square_side, self.square_side, self.square_side), 1)


    def draw_board(self):
        self.window.fill(self.background_color)

        i=self.square_side
        for k in self.board:
            j=0
            for l in k:
                if(l==1):
                    pygame.draw.rect(self.window, [0,255,0], pygame.Rect(j, i, self.square_side, self.square_side))
                j=j+self.square_side
            i=i+self.square_side

        self.draw_grid()
        pygame.display.update() #update the display

    def insert_piece(self):
        self.current_piece = piece(5,0)
        self.current_piece.place(self.board)
    
    def move_piece(self,x,y):
        self.current_piece.remove(self.board)
        self.current_piece.x+=x
        self.current_piece.y+=y
        self.current_piece.place(self.board)

    def rotate_piece(self):
        self.current_piece.remove(self.board)
        if(self.current_piece.rotation!=3):
            self.current_piece.rotation+=1
        else:
            self.current_piece.rotation=0
        self.current_piece.place(self.board)

    def move_down(self):
        i=self.current_piece.get_x()
        j=self.current_piece.get_y()
        for k in range(4):
            if(j[k]==19):
                self.new_piece=True
                self.current_piece = None
            else:
                if(self.board[j[k]+1][i[k]]==1 and not check_pair_in_list(i,j,i[k],j[k]+1,4)):
                    self.new_piece=True
                    if(j[k]==1 or j[k]==0 or j[k]==3):
                        self.current_piece = None
                        self.running = False #Ends the game

        if not self.new_piece:
            self.move_piece(0,1)

    def update_score(self):
        l=0
        for i in self.board:
            if i == [1,1,1,1,1,1,1,1,1,1]:
                self.points+=100
                if(self.points % 1000 == 0):
                    self.level += 1
                    self.interval = self.interval*self.intervaldrop
                    self.intervaldrop=self.intervaldrop*2
                for k in range(l):
                    self.board[l-k]=self.board[l-k-1]
                self.board[0] = [0,0,0,0,0,0,0,0,0,0]  #Por alguma razão alterar isto lixa tudo, rever bem
            l+=1         