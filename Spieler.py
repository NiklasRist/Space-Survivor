import pygame
from Spielfeld import Feld

pygame.init()
clock = pygame.time.Clock()








class Spieler():
    SpielerIMG = pygame.image.load(r"C:\Users\Mostafa Ganji\Desktop\Spiel_projekt\\space.png")
    SpielerIMG = pygame.transform.scale(SpielerIMG, (40, 40))
    x = (Feld.Spielfeld_width * 0.45)
    y = (Feld.Spielfeld_height * 0.8)
    Leben = 3
    punkte = 0
    schaden=1


    def move():
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change = +10
                
            if event.key == pygame.K_LEFT:
                x_change = -10

            if event.type == pygame.KEYUP:
                if event.key ==  pygame.K_RIGHT or  event.key == pygame.K_LEFT:
                    x_change = 0

            if x > Feld.Spielfeld_width - 40:
                x = 760
            if x < 0:
                x = 0    
                

        x_change = 0



        
        
        
        x += x_change 


    

        
    
    
    
    
#Gehören zur Steuerung:
    #if(Leben <= 0):
        #Gui.lost_text()

    
    
    
    
