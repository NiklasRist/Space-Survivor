import sys
import pygame
from spieler import Spieler
from spielfeld import Feld
from taste import verwalter
from button import Button



pygame.init()
class Gui:  
  def __init__(self, feld_obj):
    Gui.lost_font_text = pygame.font.SysFont('arial',200)
    Gui.lifeFont = pygame.font.SysFont('Verdana',400)
    Gui.spiel_fenster = pygame.display.set_mode([2*feld_obj.Spielfeld_width,feld_obj.Spielfeld_height])

  def create_Fenster(self):
    white = (255,255,255) 
    pygame.display.set_caption("Space survior")
    Gui.spiel_fenster.fill(white)

  def lost_text(self):
    over_text = self.lost_font_text.render("you lost", True, (255, 255, 255))
    self.spiel_fenster.blit(over_text, (400, 400)) 
   
  def display_lifes(self, feld_obj):
    lifeText = self.lifeFont.render("Leben : ", True, (255, 255, 255))
    self.spiel_fenster.blit(lifeText, (feld_obj.Spielfeld_width -100, feld_obj.Spielfeld_height))

  def display_text(self, px, py, text, color, size):
    font = pygame.font.SysFont(None, size)
    img = font.render(text, True, color)
    self.spiel_fenster.blit(img, (px, py))


  def display(self, obj): 
    self.spiel_fenster.blit(obj.aktuelles_bild, (obj.x,obj.y))


