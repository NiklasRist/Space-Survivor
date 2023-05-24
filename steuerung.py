import pygame
from gegner_spawnen import GegnerSpawnen
from gui import Gui
from spieler import Spieler
from shop import Shop
from npcs import Gegner
from event import 
from spielfeld import
from taste import
from leaderboard import
from speicher import
from sys import



class Steuerung():
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.Gui_1 = Gui()
        self.Shop_1 = Shop()
        self.NPCs_1 = NPCs()
        self.Gegnerspawn_1 = Gegenrspawn()
        self.Event_1 = Event()
        self.Spielfeld_1 = Spieldfeld(0,0)
        self.Spielfeld_2 = Spieldfeld(800,0)
        self.Spieler_1 = Spieler(0,0)
        self.Spieler_2 = Spieler(Spielfeld.Spielfeld_width, 0)
        self.Taste_1 = Taste()
        self.leaderboard_1 = leaderboard()
        self.speicher_1 = speicher()
        self.end = false 
        self.Gui_1.create_Fenster()
        self.game_mode=0 #0=Main Menu, 1=lokaler Mehrspieler, 2=LAN Mehrspieler, 3=Optionen

        main_loop()
    
    
    
    

        
    
    def main_Menu(self):
        game_mode=1
    
    def lokaler_Mehrspieler(self):
        self.Gui_1.create_Spielfeld(Spielfeld_1)
        self.Gui_1.create_Spielfeld(Spielfeld_2)
        self.Gui_1.Create_spieler()
        self.Gui_1.Create_spieler()

    def lan_Mehrspieler(self):
        self.Gui_1.create_Spielfeld(Spielfeld_1)
        self.Gui_1.create_Spielfeld(Spielfeld_2)
        self.Gui_1.Create_spieler()
        self.Gui_1.Create_spieler()

    def optionen(self):
        pass

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
            
            
            
           
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            self.Gui_1.Spiel_fenster.flip()
            self.clock.tick(60)     
                  
            
    
    
    
    




