import pygame

class Feld():
  def __init__(self, px, py):
    Spielfeld_width = 800
    Spielfeld_height = 800
    x=px
    y=py
    IMG = pygame.image.load(r"C:/Users/Mostafa Ganji/Desktop/Spiel_projekt//space.png")
    IMG = pygame.transform.scale(SpielerIMG, (800, 800))
    #background
    #Bild von Background
