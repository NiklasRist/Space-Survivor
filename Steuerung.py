import pygame, Gui , Spieler , Shop , NPCs , Gegnerspawn , Event , Spielfeld , Taste , leaderboard , speicher, sys



class Steuerung(){
    
    
    
    
    
    def __init__(self):
        self.pygame.init()
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
        self.Gui_1.create_Spielfeld(Spielfeld_1)
        self.Gui_1.create_Spielfeld(Spielfeld_2)
        self.Gui_1.Create_spieler()
        self.Gui_1.Create_spieler()

        main_loop()

        
    
    
    def main_loop():

        while not end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    end = True
                    pygame.quit()
                    sys.exit(0)
           
            
            
            
           
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            Gui_1.Spiel_fenster.flip()
            clock.tick(60)           
            
}

    
    
    




