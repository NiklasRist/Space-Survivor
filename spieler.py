import pygame
from spielfeld import Feld

pygame.init()









class Spieler():
    '''Die Spielerklasse'''

    def __init__(self,x,y, feld_obj):
        self.x=x
        self.y=y
        self.last_position = [x,y]
        self.size=int(0.05*feld_obj.Spielfeld_width)
        self.mittelpunkt=[self.x+int(0,5*self.size), self.y+int(0,5*self.size)]
        self.leben = 3
        self.punkte = 0
        self.schaden=1
        self.side=feld_obj.side
        self.SpielerIMG_links = pygame.image.load(".\images\TestImage.png")
        self.SpielerIMG_links = pygame.transform.scale(self.SpielerIMG_links, (self.size, self.size))
        self.SpielerIMG_links = pygame.transform.scale(self.SpielerIMG_links, (self.size, self.size))
        self.SpielerIMG_rechts = pygame.image.load(".\images\TestImage.png")
        self.SpielerIMG_rechts = pygame.transform.scale(self.SpielerIMG_rechts, (self.size, self.size))
        self.SpielerIMG_oben = pygame.image.load(".\images\TestImage.png")
        self.SpielerIMG_oben = pygame.transform.scale(self.SpielerIMG_oben, (self.size, self.size))
        
        
        self.SpielerIMG = pygame.image.load(".\images\TestImage.png")
        self.SpielerIMG = pygame.transform.scale(self.SpielerIMG, (self.size, self.size))
        self.aktuelles_bild=self.SpielerIMG
        
        self.spieler_images = ['self.SpielerIMG_links', 'self.SpielerIMG' , 'self.Aktuelles_bild']


    
    




    

        
    
    
    


    
    
    
    
