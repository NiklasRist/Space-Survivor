import pygame, Gui , Spieler , Shop , NPCs , Gegnerspawn , Event , Spielfeld , Taste , leaderboard , speicher, sys



class Steuerung(){
    
    
    clock = pygame.time.Clock()
    Spieler_1 = Spieler()
    Spieler_2 = Spieler()
    Gui_1 = Gui()
    Shop_1 = Shop()
    NPCs_1 = NPCs()
    Gegnerspawn_1 = Gegenrspawn()
    Event_1 = Event()
    Spielfeld_1 = Spieldfeld(0,0)
    Spielfeld_2 = Spieldfeld(800,0)
    Taste_1 = Taste()
    leaderboard_1 = leaderboard()
    speicher_1 = speicher()
    end = false 
    
    
    def init():
        pygame.init()
        Gui_1.create_Fenster()
        Gui_1.create_Spielfeld(Spielfeld_1)
        Gui_1.create_Spielfeld(Spielfeld_2)
        Gui_1.Creat_spieler(Spieler_1.x,Spieler_1.y)
        Spieler_2.x+=Spielfeld_2.Spielfeld_width
        Gui_1.Creat_spieler(Spieler_2.x,Spieler_2.y)

        
    
    
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

    
    
    




