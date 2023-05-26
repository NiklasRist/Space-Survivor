import pygame
class projektil:
    '''In der Klasse Projektil sind die Attribute die für die Projektilobjekte benötigt werden.'''
    def __init__(self, x, y, feld_obj, schuetze_obj, richtungsvektor) -> None:
        self.x=x
        self.y=y
        self.image=pygame.image.load(".\images\TestImage.png")
        self.image=pygame.transform.scale(self.SpielerIMG_links, (int(0.0125*feld_obj.Spielfeld_width), int(0.0125*feld_obj.Spielfeld_width)))
        self.schuetze=schuetze_obj
        self.richtungsvektor=richtungsvektor
        
        