import sys
import pygame
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
    Gui_1=0
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.Spielfeld_1 = Feld(0,0)
        self.Spielfeld_2 = Feld(self.Spielfeld_1.Spielfeld_width,0)
        self.Gui_1 = Gui(self.Spielfeld_1)
        self.Shop_1 = Shop()
        self.NPCs_1 = Gegner(self.Spielfeld_1)
        self.Gegnerspawn_1 = GegnerSpawnen()
        self.Event_1 = Event()
        self.Spieler_1 = Spieler((0.5*self.Spielfeld_1.Spielfeld_width), (self.Spielfeld_1.Spielfeld_height*0.9))
        self.Spieler_2 = Spieler((1.5*self.Spielfeld_1.Spielfeld_width), (self.Spielfeld_1.Spielfeld_height*0.9))
        self.Taste_1 = verwalter()
        self.leaderboard_1 = leaderboard()
        self.speicher_1 = Speicher()
        self.end = False 
        self.Gui_1.create_Fenster()
        self.game_mode=0 #0=Main Menu, 1=lokaler Mehrspieler, 2=LAN Mehrspieler, 3=Optionen
        self.spiel_start=True
        self.main_loop()
    
    
    
    

        
    
   

    def main_loop(self):

        while not self.end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    end = True
                    pygame.quit()
                    sys.exit(0)
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
            #erstellt beide Spielfelder
            self.Gui_1.create_Spielfeld(self.Spielfeld_1)
            self.Gui_1.create_Spielfeld(self.Spielfeld_2)
            #erstellt beide Spieler
            self.Gui_1.Create_spieler(self.Spieler_1)
            self.Gui_1.Create_spieler(self.Spieler_2)
            #stellt den Score beider Spieler dar
            self.Gui_1.display_text(0, 0, f"Score: {self.Spieler_1.punkte}", pygame.Color(255, 255, 255, a=255), int(34*(self.Spielfeld_1.Spielfeld_width/800)))
            self.Gui_1.display_text(self.Spielfeld_1.Spielfeld_width, 0, f"Score: {self.Spieler_2.punkte}", pygame.Color(255, 255, 255, a=255), int(34*(self.Spielfeld_1.Spielfeld_width/800)))
            #stellt Leben beider Spieler dar
            self.Gui_1.display_text(self.Spielfeld_1.Spielfeld_width*0.4, 0, f"Leben: {self.Spieler_1.leben}", pygame.Color(255, 255, 255, a=255), int(34*(self.Spielfeld_1.Spielfeld_width/800)))
            self.Gui_1.display_text(self.Spielfeld_1.Spielfeld_width*1.4, 0, f"Leben: {self.Spieler_2.leben}", pygame.Color(255, 255, 255, a=255), int(34*(self.Spielfeld_1.Spielfeld_width/800)))
            #stellt Eventpunkte Spieler dar
            self.Gui_1.display_text(self.Spielfeld_1.Spielfeld_width*0.8, 0, f"Punkte: {self.Spieler_1.punkte}", pygame.Color(255, 255, 255, a=255), int(34*(self.Spielfeld_1.Spielfeld_width/800)))
            self.Gui_1.display_text(self.Spielfeld_1.Spielfeld_width*1.8, 0, f"Punkte: {self.Spieler_2.punkte}", pygame.Color(255, 255, 255, a=255), int(34*(self.Spielfeld_1.Spielfeld_width/800)))
            ''' #nur bei Spielstart
                (321)
                schießen freigeben
                Tasten freigeben
                Gegner spawnen
            '''
            self.spiel_start=False
        ''' #immer
                Spieler bewegen
                Event auslösen
                Gegner erschaffen & bewegen
                Projektil erschaffen & bewegen
                Kollision->Text aktuallisieren
        '''        

    def lan_Mehrspieler(self):
        self.Gui_1.create_Spielfeld(self.Spielfeld_1)
        self.Gui_1.create_Spielfeld(self.Spielfeld_2)
        self.Gui_1.Create_spieler(self.Spieler_1)
        self.Gui_1.Create_spieler(self.Spieler_2)

    def optionen(self):
        pass       
    
    
    
    




