import pygame
import Spielfeld

pygame.init()
clock = pygame.time.Clock()





def Bewegen():
    print("Bewegen")


class Gegner():
    GegnerIMG = pygame.image.load("gegner Bild")
    GegnerIMG = pygame.transform.scale(GegnerIMG, (30, 30))
    x = (Spielfeld.Spielfeld_width)
    y = (Spielfeld.Spielfeld_height)
    
    G_leben = 4
    def move_gegner():
        for event in pygame.event.get():
            

            if x > Spielfeld.Spielfeld_width - 40:
                x = 760
            if x < 0:
                x = 0    
                

        x_change = 0



        Spielfeld.clock.tick(60)
        
        
        x += x_change 


    

        
    
    
    
    
#Gehören zur Steuerung:
    #if(Leben <= 0):
        #Gui.lost_text()

    
    
    
    
