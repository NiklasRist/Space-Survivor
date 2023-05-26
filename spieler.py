import pygame
from spielfeld import Feld

pygame.init()









class Spieler():
    '''Die Spielerklasse'''

    def __init__(self,x, y):
        self.x=x
        self.y=y
        self.leben = 3
        self.punkte = 0
        self.schaden=1
        self.SpielerIMG_links = pygame.image.load(".\images\TestImage.png")
        self.SpielerIMG_links = pygame.transform.scale(self.SpielerIMG_links, (int(0.05*feld_obj.Spielfeld_width), int(0.05*feld_obj.Spielfeld_width)))
        self.SpielerIMG = pygame.image.load(".\images\TestImage.png")
        self.SpielerIMG = pygame.transform.scale(self.SpielerIMG, (int(0.05*feld_obj.Spielfeld_width), int(0.05*feld_obj.Spielfeld_width)))
        self.Aktuelles_bild=self.SpielerIMG
        


    
    




    

        
    
    
    


    
    
    
    
