import pygame
from taste import verwalter
import time
import math
class event:
    def __init__(self):
        self.kosten=0
    
    def get_kosten(self):
        return self.kosten
    
    def ausfuehren(self, spieler):
        pass


loch_erschinung = False
loch_erschinung_start = None
loch_erscheinung_dauer = 5
class schwartzesloch(event):
    '''Schwarzes Loch wird erscheinen und das Raum Schiff zu sich ziehen'''
    def __init__(self,side):
        self.side = side
        self.kosten=10

        loch_image = pygame.image.load(r'.\images\eclipse-2.png')
        loch_rect = loch_image.get_rect()
        loch_rect.center = (400, 200)
        
        loch_rect.x = 100
        loch_rect.y = 200

    def loch_event(self):
        global loch_erschinung
        print("Hello das loch ist da")
        loch_erschinung = True
        loch_erschinung_start = time.time()

    def berechne_vektor(self, obj_1, obj_2):
        '''Berechnet einen Richtungsvektor aus den Koordinaten zweier Objekte'''
        if obj_1!=obj_2:
            return obj_2.mittelpunkt[0]-obj_1.mittelpunkt[0], obj_2.mittelpunkt[1]-obj_1.mittelpunkt[1]
        else:
            return obj_1.aktueller_richtungsvektor[0]-obj_1.mittelpunkt[0], obj_1.aktueller_richtungsvektor[1]-obj_1.mittelpunkt[1]  
    def berechne_abstand(self, x, y):
        '''Berechnet den Betrag(/Abstand) eines Vektors'''
        return math.sqrt(x**2+y**2)       
    def berechne_einheitsvektor(self, x, y, abstand):
        '''Berechnet aus einem Richtungsvektor und Abstand einen Einheitsvektor'''
        if abstand==0:
            return 0,0
        else:
            return x/abstand, y/abstand  



    def move_spieler_zum_loch(self, spieler_obj, spieler_obj_2,spieler_polygon,spieler_polygon_2):
        '''Bewegt die Asteroiden und ihre Polygone um einen Einheitsvektor auf den Spieler zu.'''
        #Abstandsberechnung Gegner Spieler (Vektorrechnung)
        
        if self.side == 0:
            x,y = self.berechne_vektor(spieler_obj, self)
            abstand=self.berechne_abstand(x,y)
            if abstand>=1:
                x_change,y_change=self.berechne_einheitsvektor(x,y,abstand)
                spieler_obj.x+=x_change
                spieler_obj.y+=y_change
                spieler_obj.mittelpunkt= spieler_polygon.mittelpunkt
                spieler_polygon.move_polygon([x_change, y_change]) 

        if self.side==1:
            x,y = self.berechne_vektor(spieler_obj_2, self)
            abstand=self.berechne_abstand(x,y)
            if abstand>=1:
                x_change,y_change=self.berechne_einheitsvektor(x,y,abstand)
                spieler_obj_2.x+=x_change
                spieler_obj_2.y+=y_change
                spieler_obj_2.mittelpunkt= spieler_polygon_2.mittelpunkt
                spieler_polygon_2.move_polygon([x_change, y_change]) 


    #if der spieler den event aktiviert:
    # loch_event        


class verwirrung(event):
    '''die Keys werden vertauscht'''
    def __init__(self):
        self.kosten=10
    def key_änderung(self,steuerung_obj,spieler_obj):
        if spieler_obj.side ==0 :
            steuerung_obj.spieler_1_rechts = pygame.K_LEFT
            steuerung_obj.spieler_1_links = pygame.K_RIGHT
            steuerung_obj.spieler_1_oben = pygame.K_DOWN
            steuerung_obj.spieler_1_unten = pygame.K_UP
        if spieler_obj.side == 1:         
            steuerung_obj.spieler_2_rechts = pygame.K_a
            steuerung_obj.spieler_2_links = pygame.K_d
            steuerung_obj.spieler_2_oben = pygame.K_s
            steuerung_obj.spieler_2_unten = pygame.K_w 


class event_4(event):
    "ist die "
