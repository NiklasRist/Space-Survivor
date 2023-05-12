import pygame
import Spieler
import Spielfeld
import sys

pygame.init()

lost_font_text = pygame.font.SysFont('arial',200)
live = pygame.font.SysFont('Verdana',400)



def create_Fenster():
  white = (255,255,255)
  Spielfeld = pygame.display.set_mode([2*Spielfeld.Spielfeld_width,2*Spielfeld.Spielfeld_height])
  pygame.display.set_caption("Space survior")
  Spielfeld.fill(white)

def Creat_spieler(x,y):
  Spielfeld.blit(Spieler.SpielerIMG, (Spieler.x,Spieler.y))


def lost_text():
  over_text = lost_font_text.render("you lost", True, (255, 255, 255))
    Spielfeld.blit(over_text, (400, 400)) 

    
def lives():
  livee = live.render("Leben : ", True, (255, 255, 255))
  Spielfeld.blit(livee, (Spielfeld.Spielfeld_width -100, Spielfeld.Spielfeld_height))


end = False

while not end:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      end == True
      pygame.quit()
      sys.exit(0)
      
      
      
      
    Spielfeld
    Spieler
    
    
  pygame.display.update()
