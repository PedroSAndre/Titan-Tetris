#Class to read or create the config file for the game (includes window height and width)

class config():
    def __init__(self):
        try:
            file = open('config.txt','r')
            for i in file.readlines():
                i = i.split(':')
                if('Window_width' in i[0]):
                    self.window_width = int(i[1])
                if('Window_height' in i[0]):
                    self.window_height = int(i[1])
        except Exception as e:
            if isinstance(e, ValueError) or isinstance(e, IOError):
                print('It wasn\'t possible to read the config file\nGoing back to default values')
                try:
                    file = open('config.txt','w')
                    file.write('Window_width: 750\nWindow_height: 500')
                    self.window_width = 750
                    self.window_height = 500
                except IOError:
                    print('Fatal error creating config file\nPlease verify that you have read and write permissions')
                    exit(0)

