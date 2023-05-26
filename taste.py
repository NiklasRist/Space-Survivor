import pygame
from spieler import Spieler
from spielfeld import Feld
import sys
 


pygame.init()
class verwalter:
    
    def __init__(self):
        pass

    def react_input(self, end, spieler_object, feld_obj):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                end = True
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                print(event.__dict__)
                print(event.__dict__["key"] == 97)
                print(event.__dict__["key"] == 1073742051)
               # print(spieler_object.x)
                if feld_obj.side == 0:
                    if event.__dict__["key"] == 1073741903: #keycode von K_RIGHT
                        spieler_object.x += 10
                        spieler_object.SpielerIMG_rechts = spieler_object.Aktuelles_bild 
                    if event.__dict__["key"] == 1073741904: #keycode von K_LEFT
                        spieler_object.x -= 10
                        spieler_object.SpielerIMG_links = spieler_object.Aktuelles_bild
                else:
                    if event.__dict__["key"] == 1073741903:#100: #keycode von K_a
                        spieler_object.x += 10
                        print("Hey")
                    if event.__dict__["key"] == 97: #keycode von K_a
                        spieler_object.x -= 10
            if event.type == pygame.KEYUP:
                if feld_obj.side == 0:
                    if (event.__dict__["key"] ==  pygame.K_RIGHT or  event.__dict__["key"] == pygame.K_LEFT):
                        spieler_object.SpielerIMG_oben = spieler_object.Aktuelles_bild
                else:
                    if (event.__dict__["key"] ==  pygame.K_RIGHT or  event.__dict__["key"] == pygame.K_LEFT):
                        spieler_object.SpielerIMG_oben = spieler_object.Aktuelles_bild
                    
            if spieler_object.x > feld_obj.Spielfeld_width-int(0.05*feld_obj.Spielfeld_width):
                spieler_object.x = feld_obj.Spielfeld_width-int(0.05*feld_obj.Spielfeld_width)
            if spieler_object.x < feld_obj.x:
                spieler_object.x =feld_obj.x
            if spieler_object.y > feld_obj.Spielfeld_height-int(0.05*feld_obj.Spielfeld_height):
                spieler_object.y = feld_obj.Spielfeld_height-int(0.05*feld_obj.Spielfeld_height)
            if spieler_object.y < feld_obj.y:
                spieler_object.y =feld_obj.y    
                
                                                 
            
