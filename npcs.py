import pygame
from spielfeld import Feld
import random
pygame.init()
clock = pygame.time.Clock()



class Gegner:
    '''gegnerische NPCs'''

    def __init__(self, feld_obj):
        self.G_leben = 4
        self.GegnerIMG = pygame.image.load(".\images\TestImage.png")
        self.GegnerIMG = pygame.transform.scale(self.GegnerIMG, (int(0.0375*feld_obj.Spielfeld_width), int(0.0375*feld_obj.Spielfeld_width)))
        self.schaden=1
        self.x = 0+feld_obj.x
        if random.randint(0,1)==1: #entscheidet von welcher Seite der Gegner kommt
            self.x+=feld_obj.Spielfeld_width-int(0.0375*feld_obj.Spielfeld_width)
        self.y = random.randint(0, feld_obj.Spielfeld_height-int(0.0375*feld_obj.Spielfeld_width))
        self.side=0 #Spielfeld_1
        if feld_obj.side==1:
            self.side=1 #Spielfeld_2

    def Bewegen(self):
        print("Bewegen")
    
    
    def move_gegner(self):
        for event in pygame.event.get():
            
            if x > Feld.Spielfeld_width - 40:
                x = 760
            if x < 0:
                x = 0    
                
        x_change = 0

        Feld.clock.tick(60)
        
        x += x_change 


    

        
    
    
    
    


    
    
    
    
