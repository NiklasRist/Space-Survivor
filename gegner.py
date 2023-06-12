import pygame
from spielfeld import Feld
import random

pygame.init()


class Gegner():
    

    def __init__(self, feld_obj):


        self.leben = 1
        self.size=int(0.05*feld_obj.Spielfeld_width)
        self.schaden = 1
        

        self.gegner_img = pygame.image.load(".\images\gegner.png") 
        self.gegner_img = pygame.transform.scale(self.gegner_img, (self.size, self.size))
        self.aktuelles_bild=self.gegner_img
        #bestimmt von wo bis wo in x ache der Gegener kommen darf
        self.x = random.randrange(feld_obj.x,feld_obj.x+feld_obj.Spielfeld_width)
        self.y = -500
        self.gegner_speed = 8
        self.mittelpunkt=[int(self.x+(34/64)*self.size), int(self.y+(44/64)*self.size)]

        #wird aufgerufen...(muss in steuerung)
       
        #self.y += self.gegner_speed 
        self.aktueller_richtungsvektor = [0,0]

        if self.y > feld_obj.Spielfeld_height:
            pass #den code von asteroiden, dass die gegnern sich annähren muss hier geschrieben werden
            self.x = random.randrange(0,feld_obj.Spielfeld_width)


        
        self.side = feld_obj.side





