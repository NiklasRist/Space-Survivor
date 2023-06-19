import sys
import pygame
from spieler import spieler
from spielfeld import feld
from taste import verwalter

pygame.init()

class gui:
    def __init__(self, feld_obj_2):
        """
        Initialisiert eine Instanz der Klasse gui.
        
        Args:
            feld_obj_2: Ein Objekt der Klasse feld.
        """
        gui.lost_font_text = pygame.font.SysFont('arial', 200)
        gui.lifeFont = pygame.font.SysFont('Verdana', 400)
        gui.spiel_fenster = pygame.display.set_mode([2*feld_obj_2.spielfeld_width, feld_obj_2.spielfeld_height])

    def create_fenster(self):
        """
        Erstellt das Fenster für das Spiel.
        """
        white = (255, 255, 255) 
        pygame.display.set_caption("Space survivor")

    def display_text(self, px, py, text, color, size):
        """
        Zeigt Text im Spiel an.
        
        Args:
            px: Die x-Koordinate der Textposition.
            py: Die y-Koordinate der Textposition.
            text: Der anzuzeigende Text.
            color: Die Farbe des Texts.
            size: Die Größe des Texts.
        """
        font = pygame.font.SysFont("arial", size)
        img = font.render(text, True, color)
        self.spiel_fenster.blit(img, (px, py))

    def display(self, obj):
        """
        Zeigt ein Objekt im Spiel an.
        
        Args:
            obj: Das Objekt, das angezeigt werden soll.
        """
        self.spiel_fenster.blit(obj.aktuelles_bild, (obj.x, obj.y))

    def fill(self, color):
        """
        Füllt das Spielfenster mit einer Farbe.
        
        Args:
            color: Die Farbe, mit der das Spielfenster gefüllt werden soll.
        """
        self.spiel_fenster.fill(color)
