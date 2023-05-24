import sys
import pygame
from spieler import Spieler
from spielfeld import Feld
from taste import verwalter



pygame.init()
class Gui:
  
  
  def __init__(self):
    Gui.lost_font_text = pygame.font.SysFont('arial',200)
    Gui.lifeFont = pygame.font.SysFont('Verdana',400)
    Gui.Spiel_fenster = pygame.display.set_mode([2*Feld.Spielfeld_width,Feld.Spielfeld_height])

  def create_Fenster(self):
    white = (255,255,255) 
    pygame.display.set_caption("Space survior")
    Gui.Spiel_fenster.fill(white)

  def Create_spieler(self, obj): 
    self.Spiel_fenster.blit(obj.SpielerIMG, (obj.x,obj.y))


  def lost_text(self):
    over_text = self.lost_font_text.render("you lost", True, (255, 255, 255))
    self.Spiel_fenster.blit(over_text, (400, 400)) 

      
  def display_lifes(self):
    lifeText = self.lifeFont.render("Leben : ", True, (255, 255, 255))
    self.Spiel_fenster.blit(lifeText, (Feld.Spielfeld_width -100, Feld.Spielfeld_height))

  def create_Spielfeld(self, pSpielfeld):
    self.Spiel_fenster.blit(pSpielfeld.IMG, (pSpielfeld.x, pSpielfeld.y))


