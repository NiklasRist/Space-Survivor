import pygame
from spieler import Spieler
from spielfeld import Feld
import sys
 


pygame.init()
class verwalter:
    
    def __init__(self):
        pass

    def react_input(self, end, spieler_object, spieler_object_2, feld_obj, feld_obj_2):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                end = True
                pygame.quit()
                sys.exit(0)
                
            if event.type == pygame.KEYDOWN:
                
                if event.__dict__["key"] == 1073741903: #keycode von K_RIGHT
                    spieler_object.x += 10
                    spieler_object.SpielerIMG_rechts = spieler_object.Aktuelles_bild 
                if event.__dict__["key"] == 1073741904: #keycode von K_LEFT
                    spieler_object.x -= 10
                    
                    spieler_object.SpielerIMG_links = spieler_object.Aktuelles_bild
                if event.__dict__["key"] == 100: #keycode von K_a
                    spieler_object_2.x += 10
                if event.__dict__["key"] == 97: #keycode von K_a
                    spieler_object_2.x -= 10
                    
            if event.type == pygame.KEYUP:
                
                if (event.__dict__["key"] ==  pygame.K_RIGHT or  event.__dict__["key"] == pygame.K_LEFT):
                    spieler_object.SpielerIMG_oben = spieler_object.Aktuelles_bild
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
                  
            if spieler_object_2.x > feld_obj_2.x + feld_obj_2.Spielfeld_width-int(0.05*feld_obj_2.Spielfeld_width):
                spieler_object_2.x = feld_obj_2.x + feld_obj_2.Spielfeld_width-int(0.05*feld_obj_2.Spielfeld_width)
            if spieler_object_2.x < feld_obj_2.x:
                spieler_object_2.x = feld_obj_2.x
            if spieler_object_2.y > feld_obj_2.Spielfeld_height-int(0.05*feld_obj_2.Spielfeld_height):
                spieler_object_2.y = feld_obj_2.Spielfeld_height-int(0.05*feld_obj_2.Spielfeld_height)
            if spieler_object_2.y < feld_obj_2.y:
                spieler_object_2.y =feld_obj_2.y  
                
                                                 
            
