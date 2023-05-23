import pygame
from Spielfeld import Feld

pygame.init()
clock = pygame.time.Clock()








class Spieler():
    SpielerIMG = pygame.image.load(r"C:/Users/Mostafa Ganji/Desktop/Spiel_projekt//space.png")
    SpielerIMG = pygame.transform.scale(SpielerIMG, (40, 40))
    
    SpielerIMG_links = pygame.image.load(r"C:/Users/Mostafa Ganji/Desktop/Spiel_projekt//space.png")
    SpielerIMG_links = pygame.transform.scale(SpielerIMG_links, (40, 40))
    
    Aktuelles_bild = pygame.transform.scale(Aktuelles_Bild, (40, 40))
    
    
    
    
    x = (Feld.Spielfeld_width * 0.45)
    y = (Feld.Spielfeld_height * 0.8)
    Leben = 3
    punkte = 0
    schaden=1





    

        
    
    
    
    
#Gehören zur Steuerung:
    #if(Leben <= 0):
        #Gui.lost_text()

    
    
    
    
