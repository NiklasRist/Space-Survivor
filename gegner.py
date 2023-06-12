import pygame
from spielfeld import Feld
import random

pygame.init()


class Gegner():
    

    def __init__(self, feld_obj):


        self.leben = 1
        self.size_gegner=int(0.05*feld_obj.Spielfeld_width)
        self.schaden = 1
        

        self.gegner_IMG = pygame.image.load(".\images\gegner.png") 
        self.gegner_IMG = pygame.transform.scale(self.gegner_IMG, (self.size_gegner, self.size_gegner))

        #bestimmt von wo bis wo in x ache der Gegener kommen darf
        self.x = random.randrange(0,feld_obj.Spielfeld_width)
        self.y = -500
        self.gegner_speed = 8


        #wird aufgerufen...(muss in steuerung)
       
        self.y += self.gegner_speed 


        if self.y > feld_obj.Spielfeld_height:
            pass #den code von asteroiden, dass die gegnern sich annähren muss hier geschrieben werden
            self.x = random.randrange(0,feld_obj.Spielfeld_width)

        #mit self.x ist der x koordinate von spieler gemeint
        if x > self.x and x < self.x + self.size_gegner or x + self.size > self.x or x + self.size < self.x + self.size_gegner:
            self.leben = self.leben - 1
            if self.leben == 0:
                self.score = 1


        
        self.side = feld_obj.side





