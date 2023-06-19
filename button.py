import sys
import pygame

class button():
    """
    Represents a button in the game.
    """
    def __init__(self, x, y, width, height, unpressed_img, pressed_img, label):
        """
        Initializes a new instance of the Button class.

        Args:
            x (int): The x-coordinate of the button.
            y (int): The y-coordinate of the button.
            width (int): The width of the button.
            height (int): The height of the button.
            unpressed_img (pygame.Surface): The image of the button when it's not pressed.
            pressed_img (pygame.Surface): The image of the button when it's pressed.
            label (str): The label or text associated with the button.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.unpressed_img = unpressed_img
        self.pressed_img = pressed_img
        self.img = self.unpressed_img
        self.label = label

    def draw(self, screen):
        """
        Draws the button on the screen.

        Args:
            screen (pygame.Surface): The screen or surface on which to draw the button.
        """
        screen.spiel_fenster.blit(self.img, self.rect)
        
