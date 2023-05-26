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
        self.Spieler_2 = Spieler((1.5*self.Spielfeld_1.Spielfeld_width), (self.Spielfeld_1.Spielfeld_height*0.5), self.Spielfeld_1)
        self.Taste_1 = verwalter()
        self.leaderboard_1 = leaderboard()
        self.speicher_1 = Speicher()
        self.end = False 
        self.game_mode=0 #0=Main Menu, 1=lokaler Mehrspieler, 2=LAN Mehrspieler, 3=Optionen
        self.spiel_start=True
        self.gegner=[[],[]] #[0]=side, [1]=Gegner Objekt
        self.maximale_Gegneranzahl=15
        self.main_loop()
        
    
    
    
    

        
    
   

    def main_loop(self):
        self.Gui_1.create_Fenster()
        while not self.end:
            self.Taste_1.react_input(self.end, self.Spieler_1, self.Spieler_2, self.Spielfeld_1, self.Spielfeld_2)
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
        if len(self.gegner[1])<self.maximale_Gegneranzahl*2:
            self.create_enemy(self.Spielfeld_1)
            self.create_enemy(self.Spielfeld_2)
        
        self.move_gegner(self.Spieler_1, self.Spieler_2)
        self.update_screen_1()
        
        ''' #nur bei Spielstart
                (321)
                schießen freigeben
                Tasten freigeben
            #immer
                Spieler bewegen
                Event auslösen
                Gegner erschaffen & bewegen
                Projektil erschaffen & bewegen
                Kollision->Text aktuallisieren
        '''        

    def lan_Mehrspieler(self):
        pass

    def optionen(self):
        pass       
    
    def create_enemy(self, feld_obj):
        self.gegner[0].append(feld_obj.side)
        self.gegner[1].append(Gegner(feld_obj))
        self.Gui_1.display_gegner(self.gegner[1][len(self.gegner[0])-1])

    
    def update_screen_1(self): #1 = game_mode
        #erstellt beide Spielfelder
        self.Gui_1.display_Spielfeld(self.Spielfeld_1)
        self.Gui_1.display_Spielfeld(self.Spielfeld_2)
        #erstellt beide Spieler
        self.Gui_1.display_spieler(self.Spieler_1)
        self.Gui_1.display_spieler(self.Spieler_2)
        #stellt alle Gegner dar
        for gegner in self.gegner[1]:
            self.Gui_1.display_gegner(gegner)
        #stellt den Score beider Spieler dar
        self.Gui_1.display_text(0, 0, f"Score: {self.Spieler_1.punkte}", pygame.Color(255, 255, 255, a=255), int(34*(self.Spielfeld_1.Spielfeld_width/800)))
        self.Gui_1.display_text(self.Spielfeld_1.Spielfeld_width, 0, f"Score: {self.Spieler_2.punkte}", pygame.Color(255, 255, 255, a=255), int(34*(self.Spielfeld_1.Spielfeld_width/800)))
        #stellt Leben beider Spieler dar
        self.Gui_1.display_text(self.Spielfeld_1.Spielfeld_width*0.4, 0, f"Leben: {self.Spieler_1.leben}", pygame.Color(255, 255, 255, a=255), int(34*(self.Spielfeld_1.Spielfeld_width/800)))
        self.Gui_1.display_text(self.Spielfeld_1.Spielfeld_width*1.4, 0, f"Leben: {self.Spieler_2.leben}", pygame.Color(255, 255, 255, a=255), int(34*(self.Spielfeld_1.Spielfeld_width/800)))
        #stellt Eventpunkte Spieler dar
        self.Gui_1.display_text(self.Spielfeld_1.Spielfeld_width*0.8, 0, f"Punkte: {self.Spieler_1.punkte}", pygame.Color(255, 255, 255, a=255), int(34*(self.Spielfeld_1.Spielfeld_width/800)))
        self.Gui_1.display_text(self.Spielfeld_1.Spielfeld_width*1.8, 0, f"Punkte: {self.Spieler_2.punkte}", pygame.Color(255, 255, 255, a=255), int(34*(self.Spielfeld_1.Spielfeld_width/800)))
        


    def move_gegner(self, spieler_obj, spieler_obj_2):
        for gegner in self.gegner[1]:
            x=0
            y=0
        #Abstandsberechnung Gegner Spieler (Vektorrechnung)
            print(self.gegner[1].index(gegner))
            if self.gegner[0][self.gegner[1].index(gegner)]==0:
                x=gegner.x-spieler_obj.x
                y=gegner.y-spieler_obj.y
            if self.gegner[0][self.gegner[1].index(gegner)]==1:
                x=gegner.x-spieler_obj_2.x
                y=gegner.y-spieler_obj_2.y  
            comb=x**2+y**2
            abstand=math.sqrt(comb)
            if abstand>0:
                #einheitsvektor berechnen
                x=x/abstand
                y=y/abstand
                gegner.x-=x
                gegner.y-=y