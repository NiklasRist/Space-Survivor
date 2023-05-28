import pygame
from spieler import Spieler
from spielfeld import Feld
import sys
 


pygame.init()
class verwalter:
    
    def __init__(self):
        self.x_spieler1 = 0
        self.x_spieler2 = 0
        self.x1 = 0
        self.x2 = 0

    def react_input(self, end, spieler_object, spieler_object_2, feld_obj, feld_obj_2):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                pygame.quit()
                sys.exit(0)
                
            if event.type == pygame.KEYDOWN:
                
                if event.__dict__["key"] == pygame.K_RIGHT: #keycode von K_RIGHT
                    self.x_spieler1 += 10
                    spieler_object.aktuelles_bild = spieler_object.SpielerIMG_rechts
                if event.__dict__["key"] == pygame.K_LEFT: #keycode von K_LEFT
                    self.x_spieler1 -= 10
                    spieler_object.aktuelles_bild = spieler_object.SpielerIMG_links 
                if event.__dict__["key"] == pygame.K_d: #keycode von K_a
                    self.x_spieler2 += 10
                if event.__dict__["key"] == pygame.K_a: #keycode von K_a
                    self.x_spieler2 -= 10
                    
            if event.type == pygame.KEYUP:
                
                if (event.__dict__["key"] ==  pygame.K_RIGHT or  event.__dict__["key"] == pygame.K_LEFT):
                    spieler_object.aktuelles_bild = spieler_object.SpielerIMG
                    self.x_spieler1 = 0
                if (event.__dict__["key"] ==  pygame.K_a or  event.__dict__["key"] == pygame.K_d):
                    spieler_object.aktuelles_bild = spieler_object.SpielerIMG
                    self.x_spieler2 = 0
            

                 



        
        spieler_object.last_position=spieler_object.x, spieler_object.y
        spieler_object_2.last_position=spieler_object_2.x, spieler_object_2.y
        spieler_object.x += self.x_spieler1
        spieler_object_2.x += self.x_spieler2  
        
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
            
