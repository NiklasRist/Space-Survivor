import pygame
import tkinter

root=tkinter.Tk()
class feld():
  
  def __init__(self, px, py, side):
    self.spielfeld_width = root.winfo_screenwidth()/2
    self.spielfeld_height = root.winfo_screenheight()
    self.x=px
    self.y=py
    self.IMG = pygame.image.load(".\images\stage-back.png")
    self.IMG = pygame.transform.scale(self.IMG, (self.spielfeld_width, self.spielfeld_height))
    self.aktuelles_bild=self.IMG
    self.side=side
    
    #background
    #Bild von Background

  
