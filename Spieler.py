import pygame
from Spielfeld import *

class Spieler1():

    pygame.init()

    SpielerIMG = pygame.image.load(r"C:\Users\LENOVO\Desktop\spacesurvivor\Bilder\\space.png")
    SpielerIMG = pygame.transform.scale(SpielerIMG, (40, 40))



    def Spaceship(x,y):
     Spielfeld.Spielfeld.blit(SpielerIMG, (x,y))


     x = (Spielfeld.Spielfeld_width * 0.45)
     y = (Spielfeld.Spielfeld_height * 0.8)

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
        Spielfeld.fill(Spielfeld.white)
        SpielerIMG(x,y)
        x += x_change 




    Leben = 3

    

    
    lost_font_text = pygame.font.Font('Verdana',200)
    def lost_text():
        over_text = lost_font_text.render("You have lost", True, (255, 255, 255))
        screen.blit(over_text, (400, 400)) 

    
    
    def lives(x, y):
        live = font.render("Leben : " + str(Leben), True, (255, 255, 255))
        screen.blit(live, (Spielfeld.Spielfeld_width -100, Spielfeld.Spielfeld_height))    
    
    
    

    if(Leben <= 0):
        lost_text()

    
    
    
    pygame.display.update()    
