import pygame
class projektil:
    """
    Represents a projectile in the game.
    """
    def __init__(self, x, y, feld_obj_2, schuetze_obj, richtungsvektor) -> None:
        """
        Initializes a new instance of the Projektil class.

        Args:
            x (int): The x-coordinate of the projectile.
            y (int): The y-coordinate of the projectile.
            feld_obj_2 (Feld): The field object representing the game field.
            schuetze_obj (Schuetze): The shooter object associated with the projectile.
            richtungsvektor (Tuple[int, int]): The direction vector of the projectile.
        """
        self.x=x
        self.y=y
        self.size=int(0.0125*feld_obj_2.spielfeld_width)
        self.mittelpunkt=[self.x+0.5*self.size, self.y+0.5*self.size]
        self.side=feld_obj_2.side
        self.image=pygame.image.load(".\images\projectile_normal.png")
        self.image=pygame.transform.scale(self.image, (self.size, self.size))
        self.aktuelles_bild=self.image
        self.schuetze=schuetze_obj
        self.richtungsvektor=richtungsvektor
        
        