import pygame
from spielfeld import Feld
import random

pygame.init()


class Gegner():
    

    def gegner(self, feld_obj,x ,y):
        self.x = x
        self.y = y


        self.leben = 1
        self.size_gegner=int(0.05*feld_obj.Spielfeld_width)
        self.schaden = 1
        

        self.gegner_IMG = pygame.image.load(".\images\gegner.png") 
        self.gegner_IMG = pygame.transform.scale(self.gegner_IMG, (self.size_gegner, self.size_gegner))

        #bestimmt von wo bis wo in x ache der Gegener kommen darf
        self.gegner_startx = random.randrange(0,feld_obj.Spielfeld_width)
        self.gegner_starty = -500
        self.gegner_speed = 8


        #wird aufgerufen...(muss in steuerung)
        self.gegner(self.gegner_startx,self.gegner_starty,self.x,self.y)
        self.gegner_starty += self.gegner_speed 


        if self.gegner_starty > feld_obj.Spielfeld_height:
            pass #den code von asteroiden, dass die gegnern sich annähren muss hier geschrieben werden
            self.gegner_startx = random.randrange(0,feld_obj.Spielfeld_width)

        #mit self.x ist der x koordinate von spieler gemeint
        if x > self.gegner_startx and x < self.gegner_startx + self.size_gegner or x + self.size > self.gegner_startx or x + self.size < self.gegner_startx + self.size_gegner:
            self.leben = self.leben - 1
            if self.leben == 0:
                self.score = 1


        






