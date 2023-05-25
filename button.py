import sys
import pygame

class button():

    def __init__(self, px, py, width, height, button_txt, onclick_function=None, one_press=False):
            self.button_text = button_txt
            self.x = px
            self.y = py
            self.width = width
            self.height = height
            self.onclick_function = onclick_function
            self.one_press = one_press
            self.already_pressed = False

            self.fill_colors = {
                'normal': '#ffffff',
                'hover': '#666666',
                'pressed': '#333333',
            }

            self.button_surface = pygame.Surface((self.width, self.height))
            self.button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

            self.button_surf = font.render(button_txt, True, (20, 20, 20))

            objects.append(self)
