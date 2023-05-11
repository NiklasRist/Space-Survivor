import pygame
import Spieler
import Spielfeld
import sys

pygame.init()


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
