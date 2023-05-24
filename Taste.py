import pygame
from Spieler import Spieler
from Spielfeld import Feld
 


pygame.init()
class verwalter:
    Spieler.SpielerIMG_links = Spieler.Aktuelles_bild
    Spieler.SpielerIMG = Spieler.SpielerIMG_links
    Spieler.Aktuelles_bild = Spieler.SpielerIMG
    def move_Spieler1():
        
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


    def move_Spieler2():
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



