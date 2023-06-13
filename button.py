import sys
import pygame

class Button():

    def __init__(self, x, y, width, height, unpressed_img, pressed_img, label):
        self.rect = pygame.Rect(x, y, width, height)
        self.unpressed_img = unpressed_img
        self.pressed_img = pressed_img
        self.img = self.unpressed_img
        self.label = label

    def check_collision(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.img = self.pressed_img
            print(f"Button '{self.label}' clicked!")
            self.perform_action()
        else:
            self.img = self.unpressed_img

    def perform_action(self):
        if self.label == 'menue_button':
            return 0
        elif self.label == 'play_local_button':
            return 1
        elif self.label == 'play_lan_button':
            return 2
        elif self.label == 'score_button':
            return 3

    def draw(self, screen):
        screen.spiel_fenster.blit(self.img, self.rect)
