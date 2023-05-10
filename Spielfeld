import pygame
from Spieler import * 


Spielfeld_width = 800
Spielfeld_height = 800


clock = pygame.time.Clock()


Spielfeld = pygame.display.set_mode([Spielfeld_width,Spielfeld_height])
pygame.display.set_caption("Space survior")



end = False

while not end:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      end == True
      Spieler1 = Spieler.Spieler1()
      pygame.quit()
      
      
  pygame.display.update()



#farben:
white = (255,255,255)
