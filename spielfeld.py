import pygame
import tkinter

root=tkinter.Tk()
class Feld():
  
  def __init__(self, px, py, side):
    self.Spielfeld_width = root.winfo_screenwidth()/2
    self.Spielfeld_height = root.winfo_screenheight()
    self.x=px
    self.y=py
    self.IMG = pygame.image.load(".\images\TestImage.png")
    self.IMG = pygame.transform.scale(self.IMG, (self.Spielfeld_width, self.Spielfeld_height))
    self.aktuelles_bild=self.IMG
    self.side=side
    
    #background
    #Bild von Background

  
