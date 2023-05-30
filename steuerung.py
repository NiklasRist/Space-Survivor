import sys
import pygame
import math
from gegner_spawnen import GegnerSpawnen
from gui import Gui
from spieler import Spieler
from shop import Shop
from npcs import Gegner
from event import Event
from spielfeld import Feld
from taste import verwalter
from leaderboard import leaderboard
from speicher import Speicher
from projektil import projektil





class Steuerung():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.Spielfeld_1 = Feld(0,0,0)
        self.Spielfeld_2 = Feld(self.Spielfeld_1.Spielfeld_width,0,1)
        self.Gui_1 = Gui(self.Spielfeld_1)
        self.Shop_1 = Shop()
        self.Gegnerspawn_1 = GegnerSpawnen()
        self.Event_1 = Event()
        self.Spieler_1 = Spieler((0.5*self.Spielfeld_1.Spielfeld_width), (self.Spielfeld_1.Spielfeld_height*0.5), self.Spielfeld_1)
        self.Spieler_2 = Spieler((1.5*self.Spielfeld_2.Spielfeld_width), (self.Spielfeld_2.Spielfeld_height*0.5), self.Spielfeld_2)
        self.Taste_1 = verwalter()
        self.leaderboard_1 = leaderboard()
        self.speicher_1 = Speicher()
        self.projektile=[]
        self.end = False 
        self.game_mode=0 #0=Main Menu, 1=lokaler Mehrspieler, 2=LAN Mehrspieler, 3=Optionen
        self.spiel_start=True
        self.gegner=[] 
        self.maximale_Gegneranzahl=15
        self.maximale_projektil_anzahl=30
        self.count=0
        self.text_size=int(34*(self.Spielfeld_1.Spielfeld_width/800))
        self.main_loop()

    def main_loop(self):
        self.Gui_1.create_Fenster()
        while not self.end:
            if self.game_mode==0:
                self.main_Menu()
            elif self.game_mode==1:
                self.lokaler_Mehrspieler()
            elif self.game_mode==2:
                self.lan_Mehrspieler()
            elif self.game_mode==3:
                self.optionen()
            else:
                self.game_mode=0
            
            pygame.display.flip()
            self.clock.tick(60)     
                  
    def main_Menu(self):
        self.game_mode=1
        self.spiel_start=True
        '''
            3 Buttons die game_mode verändern
        '''
    
    def lokaler_Mehrspieler(self):
        
        if self.spiel_start:
            pass
        self.spiel_start=False
        
        #erschafft Gegner, darf nicht jedes mal passieren, Gegner müssen sich auf Spieler zubewegen
        if len(self.gegner)<self.maximale_Gegneranzahl*2:
            self.create_enemy(self.Spielfeld_1)
            self.create_enemy(self.Spielfeld_2)
        
        if self.count==5:
                self.create_projectile(self.Spielfeld_1, self.Spieler_1)
                self.create_projectile(self.Spielfeld_2, self.Spieler_2)
                self.count=0
                if self.maximale_projektil_anzahl<len(self.projektile):
                    self.projektile.pop(0)
                    self.projektile.pop(0)
        else:
            self.count+=1
        
        
        self.move_projectile(self.Spieler_1, self.Spieler_2)
        self.Taste_1.react_input(self.end, self.Spieler_2, self.Spieler_1, self.Spielfeld_1, self.Spielfeld_2)
        self.move_gegner(self.Spieler_1, self.Spieler_2)
        self.update_screen_1()
        
        ''' #nur bei Spielstart
                (321)
                schießen freigeben
                Tasten freigeben
            #immer
                Event auslösen
                Projektil erschaffen & bewegen
                Kollision->Text aktuallisieren
        '''        

    def lan_Mehrspieler(self):
        pass

    def optionen(self):
        pass       
    
    def create_enemy(self, feld_obj):
        self.gegner.append(Gegner(feld_obj))
        self.Gui_1.display(self.gegner[len(self.gegner)-1])

    def create_projectile(self, feld_obj, schuetze_obj): #Richtungsvektor ändert sich bei zu kleinen Bewegungen nicht, mögliche Lösung kopiere den letzten Richtungsvektor aus Verwalter
        self.projektile.append(projektil(schuetze_obj.mittelpunkt[0], schuetze_obj.mittelpunkt[1], feld_obj, schuetze_obj, [2*schuetze_obj.aktueller_richtungsvektor[0], 2*schuetze_obj.aktueller_richtungsvektor[1]]))
        self.Gui_1.display(self.projektile[len(self.projektile)-1])
    
    def update_screen_1(self): #1 = game_mode
        #erstellt beide Spielfelder
        self.Gui_1.display(self.Spielfeld_1)
        self.Gui_1.display(self.Spielfeld_2)
        #erstellt beide Spieler
        self.Gui_1.display(self.Spieler_1)
        self.Gui_1.display(self.Spieler_2)
        #stellt alle Gegner dar
        for gegner in self.gegner:
            self.Gui_1.display(gegner)
        #stellt alle Projektile dar
        for projectile in self.projektile:
            self.Gui_1.display(projectile)
        #stellt den Score beider Spieler dar
        self.Gui_1.display_text(0, 0, f"Score: {self.Spieler_1.punkte}", pygame.Color(255, 255, 255, a=255), self.text_size)
        self.Gui_1.display_text(self.Spielfeld_1.Spielfeld_width, 0, f"Score: {self.Spieler_2.punkte}", pygame.Color(255, 255, 255, a=255), self.text_size)
        #stellt Leben beider Spieler dar
        self.Gui_1.display_text(self.Spielfeld_1.Spielfeld_width*0.4, 0, f"Leben: {self.Spieler_1.leben}", pygame.Color(255, 255, 255, a=255), self.text_size)
        self.Gui_1.display_text(self.Spielfeld_1.Spielfeld_width*1.4, 0, f"Leben: {self.Spieler_2.leben}", pygame.Color(255, 255, 255, a=255), self.text_size)
        #stellt Eventpunkte Spieler dar
        self.Gui_1.display_text(self.Spielfeld_1.Spielfeld_width*0.8, 0, f"Punkte: {self.Spieler_1.punkte}", pygame.Color(255, 255, 255, a=255), self.text_size)
        self.Gui_1.display_text(self.Spielfeld_1.Spielfeld_width*1.8, 0, f"Punkte: {self.Spieler_2.punkte}", pygame.Color(255, 255, 255, a=255), self.text_size)
        

    def move_projectile(self, spieler_obj, spieler_obj_2):
        for projectile in self.projektile:
            projectile.x-=projectile.richtungsvektor[0]
            projectile.y-=projectile.richtungsvektor[1]
            self.projectile_boundaries()
    
    def move_gegner(self, spieler_obj, spieler_obj_2):
        for gegner in self.gegner:
            x=0
            y=0
        #Abstandsberechnung Gegner Spieler (Vektorrechnung)
            if self.gegner[self.gegner.index(gegner)].side==0:
                x,y = self.berechne_vektor( gegner, spieler_obj)
            if self.gegner[self.gegner.index(gegner)].side==1:
                x,y = self.berechne_vektor( gegner,spieler_obj_2)
            abstand=self.berechne_abstand(x,y)
            if abstand>=1:
                x_change,y_change=self.berechne_einheitsvektor(x,y,abstand)
                gegner.x+=x_change
                gegner.y+=y_change
                

                
    
    def berechne_vektor(self, obj_1, obj_2):
        if obj_1!=obj_2:
            return obj_2.x-obj_1.x, obj_2.y-obj_1.y
        else:
            return obj_1.aktueller_richtungsvektor[0]-obj_1.x, obj_1.aktueller_richtungsvektor[1]-obj_1.y
   
    def berechne_abstand(self, x, y):
        return math.sqrt(x**2+y**2)
        
    def berechne_einheitsvektor(self, x, y, abstand):
        if abstand==0:
            return 0,0
        else:
            return x/abstand, y/abstand
        
    def schießen(self, x, y, feld_obj, schuetze_obj):
        einheitsvektor=self.berechne_einheitsvektor()
        self.create_projectile(x, y, feld_obj, schuetze_obj, einheitsvektor)
        
    def projectile_boundaries(self):
        for projectile in self.projektile:
            if projectile.side == self.Spielfeld_1.side:
                if projectile.x < self.Spielfeld_1.x or projectile.x > self.Spielfeld_1.x+self.Spielfeld_1.Spielfeld_width-0.0125*self.Spielfeld_1.Spielfeld_width or projectile.y < self.Spielfeld_1.y or projectile.y > self.Spielfeld_1.y+self.Spielfeld_1.Spielfeld_height:
                    self.projektile.pop(self.projektile.index(projectile))
            if projectile.side == self.Spielfeld_2.side:
                if projectile.x < self.Spielfeld_2.x or projectile.x > self.Spielfeld_2.x+self.Spielfeld_2.Spielfeld_width or projectile.y < self.Spielfeld_2.y or projectile.y > self.Spielfeld_2.y+self.Spielfeld_2.Spielfeld_height:
                    self.projektile.pop(self.projektile.index(projectile))
                    