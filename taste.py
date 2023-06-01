import pygame
from spieler import Spieler
from spielfeld import Feld
import sys
import math
 


pygame.init()
class verwalter:
    
    def __init__(self):
        self.x_spieler_1 = 0
        self.x_spieler_2 = 0
        self.x_1 = 0
        self.x_2 = 0
        self.y_spieler_1 = 0
        self.y_spieler_2 = 0
        self.y_1 = 0
        self.y_2 = 0

    def react_input(self, end, spieler_object, spieler_object_2, feld_obj, feld_obj_2):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                pygame.quit()
                sys.exit(0)
                
            if event.type == pygame.KEYDOWN:
                
                if event.__dict__["key"] == pygame.K_RIGHT: #keycode von K_RIGHT
                    self.x_spieler_1 += 10
                    spieler_object.aktuelles_bild = spieler_object.SpielerIMG_rechts
                if event.__dict__["key"] == pygame.K_LEFT: #keycode von K_LEFT
                    self.x_spieler_1 -= 10
                    spieler_object.aktuelles_bild = spieler_object.SpielerIMG_links 
                if event.__dict__["key"] == pygame.K_d: #keycode von K_d
                    self.x_spieler_2 += 10
                if event.__dict__["key"] == pygame.K_a: #keycode von K_a
                    self.x_spieler_2 -= 10
                
                
                if event.__dict__["key"] == pygame.K_DOWN: #keycode von K_DOWN
                    self.y_spieler_1 += 10                   
                if event.__dict__["key"] == pygame.K_UP: #keycode von K_UP
                    self.y_spieler_1 -= 10                   
                if event.__dict__["key"] == pygame.K_s: #keycode von K_s
                    self.y_spieler_2 += 10
                if event.__dict__["key"] == pygame.K_w: #keycode von K_w
                    self.y_spieler_2 -= 10



                    
            if event.type == pygame.KEYUP:
                
                if (event.__dict__["key"] ==  pygame.K_RIGHT or  event.__dict__["key"] == pygame.K_LEFT):
                    spieler_object.aktuelles_bild = spieler_object.SpielerIMG
                    self.x_spieler_1 = 0
                if (event.__dict__["key"] ==  pygame.K_a or  event.__dict__["key"] == pygame.K_d):
                    spieler_object.aktuelles_bild = spieler_object.SpielerIMG
                    self.x_spieler_2 = 0

            
                if (event.__dict__["key"] ==  pygame.K_UP or  event.__dict__["key"] == pygame.K_DOWN):
                    self.y_spieler_1 = 0
                if (event.__dict__["key"] ==  pygame.K_s or  event.__dict__["key"] == pygame.K_w):
                    spieler_object.aktuelles_bild = spieler_object.SpielerIMG
                    self.y_spieler_2 = 0
                 



        if math.sqrt(self.x_spieler_1**2+self.y_spieler_1**2)!=0:
            spieler_object.aktueller_richtungsvektor=self.x_spieler_1, self.y_spieler_1
        if math.sqrt(self.x_spieler_2**2+self.y_spieler_2**2)!=0:
            spieler_object_2.aktueller_richtungsvektor=self.x_spieler_2, self.y_spieler_2
        
        spieler_object.x += self.x_spieler_1
        spieler_object_2.x += self.x_spieler_2 

        spieler_object.y += self.y_spieler_1
        spieler_object_2.y += self.y_spieler_2 


        
        if spieler_object_2.x > feld_obj.Spielfeld_width- spieler_object_2.size:
            spieler_object_2.x = feld_obj.Spielfeld_width-spieler_object_2.size
        if spieler_object_2.x < feld_obj.x:
            spieler_object_2.x =feld_obj.x
        if spieler_object_2.y > feld_obj.Spielfeld_height-spieler_object_2.size:
            spieler_object_2.y = feld_obj.Spielfeld_height-spieler_object_2.size
        if spieler_object_2.y < feld_obj.y:
            spieler_object_2.y =feld_obj.y  
            
        if spieler_object.x > feld_obj_2.x + feld_obj_2.Spielfeld_width-spieler_object.size:
            spieler_object.x = feld_obj_2.x + feld_obj_2.Spielfeld_width-spieler_object.size
        if spieler_object.x < feld_obj_2.x:
            spieler_object.x = feld_obj_2.x
        if spieler_object.y > feld_obj_2.Spielfeld_height-spieler_object.size:
            spieler_object.y = feld_obj_2.Spielfeld_height-spieler_object.size
        if spieler_object.y < feld_obj_2.y:
            spieler_object.y =feld_obj_2.y   
        
        spieler_object.mittelpunkt= [spieler_object.x+0.5*spieler_object.size, spieler_object.y+0.5*spieler_object.size]   
        spieler_object_2.mittelpunkt= [spieler_object_2.x+0.5*spieler_object_2.size, spieler_object_2.y+0.5*spieler_object_2.size]                          
            
