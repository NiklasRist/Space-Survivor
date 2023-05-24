import pygame

class Feld():
  IMG = pygame.image.load(r"images\TestImage.png")
  IMG = pygame.transform.scale(IMG, (800, 800))
  def __init__(self, px, py):
    self.Spielfeld_width = 800
    self.Spielfeld_height = 800
    self.x=px
    self.y=py
    
    #background
    #Bild von Background

  
