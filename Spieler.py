import pygame
import Spielfeld

pygame.init()
clock = pygame.time.Clock()



lost_font_text = pygame.font.SysFont('arial',200)
live = pygame.font.SysFont('Verdana',400)


x = (Spielfeld.Spielfeld_width * 0.45)
y = (Spielfeld.Spielfeld_height * 0.8)


class Spieler():
    SpielerIMG = pygame.image.load(r"C:\Users\Mostafa Ganji\Desktop\Spiel_projekt\\space.png")
    SpielerIMG = pygame.transform.scale(SpielerIMG, (40, 40))


    def Spaceship(x,y):
     Spielfeld.blit(Spieler.SpielerIMG, (x,y))




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

            if x > Spielfeld.Spielfeld_width - 40:
                x = 760
            if x < 0:
                x = 0    
                

        x_change = 0



        Spielfeld.clock.tick(60)
        
        Spieler.SpielerIMG(x,y)
        x += x_change 




    Leben = 3

    
    
    def lost_text():
        over_text = lost_font_text.render("you lost", True, (255, 255, 255))
        Spielfeld.blit(over_text, (400, 400)) 

    
    
    def lives(x, y):
        live = live.render("Leben : ", True, (255, 255, 255))
        Spielfeld.blit(live, (Spielfeld.Spielfeld_width -100, Spielfeld.Spielfeld_height))    
    
    
    

    if(Leben <= 0):
        lost_text()

    
    
    
    
