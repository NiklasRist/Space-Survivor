import pygame
from spielfeld import Feld
import random
pygame.init()
clock = pygame.time.Clock()



class Gegner:
    '''gegnerische NPCs'''

    def __init__(self, feld_obj):
        self.G_leben = 4
        self.side=feld_obj.side
        self.x = 0+feld_obj.x
        self.size=int(0.0375*feld_obj.Spielfeld_width)
        if random.randint(0,1)==1: #entscheidet von welcher Seite der Gegner kommt
            self.x+=feld_obj.Spielfeld_width-self.size
        self.y = random.randint(0, feld_obj.Spielfeld_height-self.size)
        self.mittelpunkt=[self.x+0.5*self.size, self.y+0.5*self.size]
        self.GegnerIMG = pygame.image.load(r".\images\asteroid-01.png")
        self.GegnerIMG = pygame.transform.scale(self.GegnerIMG, (self.size, self.size))
        self.aktuelles_bild=self.GegnerIMG
        self.schaden=1
        

    
    



    

        
    
    
    
    


    
    
    
    
