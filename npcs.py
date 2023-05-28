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
        self.aktuelles_bild=self.GegnerIMG
        self.schaden=1
        self.side=feld_obj.side
        self.x = 0+feld_obj.x
        if random.randint(0,1)==1: #entscheidet von welcher Seite der Gegner kommt
            self.x+=feld_obj.Spielfeld_width-int(0.0375*feld_obj.Spielfeld_width)
        self.y = random.randint(0, feld_obj.Spielfeld_height-int(0.0375*feld_obj.Spielfeld_width))
        self.side=feld_obj.side
        

    
    



    

        
    
    
    
    


    
    
    
    
