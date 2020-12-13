#Class to represent a piece on a board
import random as rand

class piece():
    def __init__(self,x,y):
        self.piece=rand.randint(0,6) #generates a random piece
        self.rotation=0
        self.x=x
        self.y=y
        self.relatives = [[0,0],[0,0],[0,0]]


    #The pieces can be checked on infopiece.png on the sources folder
    def neighbour(self):
        if(self.piece==0):
            self.relatives = [[1,0],[-1,0],[-2,0]]
        if(self.piece==1):
            self.relatives = [[1,0],[0,1],[0,2]] 
        if(self.piece==2):
            self.relatives = [[-1,0],[0,1],[0,2]]
        if(self.piece==3):
            self.relatives = [[-1,0],[-1,1],[-1,1]]
        if(self.piece==4):
            self.relatives = [[1,0],[0,1],[-1,1]]
        if(self.piece==5):
            self.relatives = [[0,1],[1,0],[-1,0]]
        if(self.piece==6):
            self.relatives = [[-1,0],[0,1],[1,1]]

    def do_rotation(self):
        if(self.rotation == 1 or self.rotation == 3):
            for i in self.relatives:
                j=i[0]
                i[0]=i[1]
                i[1]=j
        if(self.rotation == 1 or self.rotation == 2):
            for i in self.relatives:
                i[0]=-i[0]
        if(self.rotation == 2 or self.rotation == 3):
            for i in self.relatives:
                i[1]=-i[1]


    def refresh(self):
        self.neighbour()
        self.do_rotation()

    def place(self, matrix):
        self.refresh()
        matrix[self.x][self.y]=1
        for i in self.relatives:
            matrix[i[0]+self.x][i[1]+self.y]=1

    def remove(self,matrix):
        matrix[self.x][self.y]=0
        for i in self.relatives:
            matrix[i[0]+self.x][i[1]+self.y]=0