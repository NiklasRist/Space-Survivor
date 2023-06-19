import pygame
import tkinter

root=tkinter.Tk()
class feld():
  """
  Represents a field in the game.
  """
  
  def __init__(self, px, py, side):
    """
    Initializes a new instance of the Feld class.

    Args:
        px (int): The x-coordinate of the field.
        py (int): The y-coordinate of the field.
        side (int): The side of the field.
    """
    self.spielfeld_width = root.winfo_screenwidth()/2
    self.spielfeld_height = root.winfo_screenheight()
    self.x=px
    self.y=py
    self.img = pygame.image.load(".\images\stage-back.png")
    self.img = pygame.transform.scale(self.img, (self.spielfeld_width, self.spielfeld_height))
    self.aktuelles_bild=self.img
    self.side=side
    
    #background
    #Bild von Background

  
