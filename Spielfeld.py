import pygame
 
white = (255,255,255)
Spielfeld_width = 800
Spielfeld_height = 800
class Spieldfeld():
  Spielfeld = pygame.display.set_mode([Spielfeld_width,Spielfeld_height])
  pygame.display.set_caption("Space survior")
  Spielfeld.fill(white)
