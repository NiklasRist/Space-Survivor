import pygame
from spielfeld import feld

pygame.init()

class spieler:
    '''
    Die Spielerklasse.

    Attributes:
        name (str): Der Name des Spielers.
        x (int): Die x-Koordinate des Spielers.
        y (int): Die y-Koordinate des Spielers.
        aktueller_richtungsvektor (list): Der aktuelle Richtungsvektor des Spielers.
        size (int): Die Größe des Spielers.
        mittelpunkt (list): Der Mittelpunkt des Spielers.
        leben (int): Die Anzahl der Leben des Spielers.
        punkte (int): Die Anzahl der Punkte des Spielers.
        score (int): Der Punktestand des Spielers.
        schaden (int): Der Schaden, den der Spieler verursacht.
        side: Die Seitenlänge des Spielfelds.
        spieler_img_links: Das Bild des Spielers in der linken Richtung.
        spieler_img_rechts: Das Bild des Spielers in der rechten Richtung.
        spieler_img: Das aktuelle Bild des Spielers.
        aktuelles_bild: Das aktuelle Bild des Spielers.
        spieler_images: Eine Liste der Bilder des Spielers.

    Methods:
        __init__(self, x, y, feld_obj_2): Initialisiert den Spieler.
    '''

    def __init__(self, x, y, feld_obj_2):
        '''
        Initialisiert den Spieler.

        Args:
            x (int): Die x-Koordinate des Spielers.
            y (int): Die y-Koordinate des Spielers.
            feld_obj_2: Ein Objekt des Spielfelds.

        Returns:
            None

        Raises:
            None
        '''
        self.name = "Edgar"
        self.x = x
        self.y = y
        self.aktueller_richtungsvektor = [0, 10]
        self.size = int(0.05 * feld_obj_2.spielfeld_width)
        self.mittelpunkt = [int(x + (24 / 48) * self.size), int(y + (30 / 48) * self.size)]
        self.leben = 3
        self.punkte = 0
        self.score = 0
        self.schaden = 1
        self.side = feld_obj_2.side
        self.spieler_img_links = pygame.image.load(".\images\spieler_stark_links.png")
        self.spieler_img_links = pygame.transform.scale(self.spieler_img_links, (self.size, self.size))
        self.spieler_img_rechts = pygame.image.load(".\images\spieler_stark_rechts.png")
        self.spieler_img_rechts = pygame.transform.scale(self.spieler_img_rechts, (self.size, self.size))
        self.spieler_img = pygame.image.load(".\images\spieler_normal.png")
        self.spieler_img = pygame.transform.scale(self.spieler_img, (self.size, self.size))
        self.aktuelles_bild = self.spieler_img
        self.spieler_images = ['self.spieler_img_links', 'self.spieler_img', 'self.Aktuelles_bild']
