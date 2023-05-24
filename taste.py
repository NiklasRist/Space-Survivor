import pygame
from spieler import Spieler
from spielfeld import Feld
 


pygame.init()
class verwalter:
    
    def __init__(self):
        pass
        
    '''@Mostafa bitte mach das als Operation mit dem jeweiligen Spielerobjekt als Input
        Spieler.SpielerIMG_links = Spieler.Aktuelles_bild
        Spieler.SpielerIMG = Spieler.SpielerIMG_links
        Spieler.Aktuelles_bild = Spieler.SpielerIMG
    '''
    def move_Spieler1(self):
        
        for event in pygame.event.get():
                    
            if pygame.event.type == pygame.KEYDOWN:
                if pygame.event.key == pygame.K_RIGHT:
                    x_change = +10
                    
                if pygame.event.key == pygame.K_LEFT:
                    x_change = -10

            if pygame.event.type == pygame.KEYUP:
                if pygame.event.key ==  pygame.K_RIGHT or  pygame.event.key == pygame.K_LEFT:
                    x_change = 0

            if x > Feld.Spielfeld_width - 40:
                x = 760
            if x < 0:
                x = 0    
                    

            x_change = 0
            
            
            x += x_change  


    def move_Spieler2(self):
        for event in pygame.event.get():
                    
            if pygame.event.type == pygame.KEYDOWN:
                if pygame.event.key == pygame.K_d:
                    x_change = +10
                    
                if pygame.event.key == pygame.K_a:
                    x_change = -10

            if pygame.event.type == pygame.KEYUP:
                if pygame.event.key ==  pygame.K_d or  pygame.event.key == pygame.K_a:
                    x_change = 0

            if x > Feld.Spielfeld_width - 40:
                x = 760
                if x < 0:
                    x = 0    
                    

            x_change = 0
            
            
            x += x_change 



