import pygame
from spielfeld import Feld

pygame.init()
clock = pygame.time.Clock()



class Gegner:
    '''gegnerische NPCs'''

    def __init__(self):
        self.G_leben = 4
        self.GegnerIMG = pygame.image.load("gegner Bild")
        self.GegnerIMG = pygame.transform.scale(self.GegnerIMG, (30, 30))
        self.x = (Feld.Spielfeld_width)
        self.y = (Feld.Spielfeld_height)
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

    
    
    
    