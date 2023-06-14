import pygame
from spielfeld import feld

pygame.init()









class spieler():
    '''Die Spielerklasse''' 

    def __init__(self,x,y, feld_obj):
        self.name="Edgar"
        self.x=x
        self.y=y
        self.aktueller_richtungsvektor = [0,10]
        self.size=int(0.05*feld_obj.spielfeld_width)
        self.mittelpunkt=[int(x+(24/48)*self.size), int(y+(30/48)*self.size)]
        self.leben = 3
        self.punkte = 0
        self.score=0
        self.schaden=1
        self.side=feld_obj.side
        self.spielerIMG_links = pygame.image.load(".\images\spieler_stark_links.png")
        self.spielerIMG_links = pygame.transform.scale(self.spielerIMG_links, (self.size, self.size))
        self.spielerIMG_rechts = pygame.image.load(".\images\spieler_stark_rechts.png")
        self.spielerIMG_rechts = pygame.transform.scale(self.spielerIMG_rechts, (self.size, self.size))
        self.spielerIMG_oben = pygame.image.load(".\images\TestImage.png")
        self.spielerIMG_oben = pygame.transform.scale(self.spielerIMG_oben, (self.size, self.size))
        
        
        self.spielerIMG = pygame.image.load(".\images\spieler_normal.png")
        self.spielerIMG = pygame.transform.scale(self.spielerIMG, (self.size, self.size))
        self.aktuelles_bild=self.spielerIMG
        
        self.spieler_images = ['self.spielerIMG_links', 'self.spielerIMG' , 'self.Aktuelles_bild']


    
    




    

        
    
    
    


    
    
    
    
