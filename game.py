#Class with all the game variables to be used
#The oficial board is 10x20, so this values cannot be changed
import pygame

class game():
    def __init__(self):
        #All variables necessary for the game
        self.level=1
        self.points=0 
        self.interval=3 #Interval in seconds between drops
        self.intervaldrop=0.25

        self.points_to_new_level=10000
        self.points_per_line_cleared=1000

        self.window=None #Needs to wait for window to be created in main loop
        self.window_width=None
        self.window_height=None
        self.square_side=None
        self.window_title='Titan Tetris'
        self.icon_path='sources/icon.png'
        self.background_color=[255,255,255] #white background color
        self.grid_color=[169,169,169] #grid lines color

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
    def start_window(self):
        pygame.init()
        self.square_side = int((self.window_width)/10)
        self.window_height = (21)*(self.square_side)
        self.window = pygame.display.set_mode([self.window_width, self.window_height])
        pygame.display.set_caption(self.window_title)
        pygame.display.set_icon(pygame.image.load(self.icon_path))

    #Function to draw grid and update the score
    def draw_grid(self):
        self.window.fill(self.background_color)
        
        for i in range(1, 21):
            for j in range(10):
                pygame.draw.rect(self.window, self.grid_color, pygame.Rect(j*self.square_side, i*self.square_side, self.square_side, self.square_side), 2)

        