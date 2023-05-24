import pygame
from Spieler import Spieler
from Spielfeld import Feld
import sys
from Taste import verwalter




pygame.init()
class Gui:
  lost_font_text = pygame.font.SysFont('arial',200)
  lifeFont = pygame.font.SysFont('Verdana',400)

  Spiel_fenster = pygame.display.set_mode([2*Feld.Spielfeld_width,Feld.Spielfeld_height])

  def create_Fenster():
    white = (255,255,255) 
    pygame.display.set_caption("Space survior")
    Spiel_fenster.fill(white)

  def Create_spieler():
    Spiel_fenster.blit(Spieler.SpielerIMG, (Spieler.x,Spieler.y))


  def lost_text():
    over_text = lost_font_text.render("you lost", True, (255, 255, 255))
    Spiel_fenster.blit(over_text, (400, 400)) 

      
  def display_lifes():
    lifeText = lifeFont.render("Leben : ", True, (255, 255, 255))
    Spiel_fenster.blit(lifeText, (Feld.Spielfeld_width -100, Feld.Spielfeld_height))

  def create_Spielfeld(pSpielfeld):
    Spiel_fenster.blit(pSpielfeld.IMG, (pSpielfeld.x, pSpielfeld.y))


