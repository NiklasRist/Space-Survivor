import pygame
from spielfeld import Feld

pygame.init()
clock = pygame.time.Clock()



class Gegner:
    '''gegnerische NPCs'''

    def __init__(self, feld_obj):
        self.G_leben = 4
        self.GegnerIMG = pygame.image.load(".\images\TestImage.png")
        self.GegnerIMG = pygame.transform.scale(self.GegnerIMG, (int(0.0375*feld_obj.Spielfeld_width), int(0.0375*feld_obj.Spielfeld_width)))
        self.x = 0
        self.y = 0
        self.schaden=1

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


    

        
    
    
    
    
#Gehören zur Steuerung:
    #if(Leben <= 0):
        #Gui.lost_text()

    
    
    
    
