import sys
import pygame

class button():

    def __init__(self, x, y, width, height, unpressed_img, pressed_img, label):
        self.rect = pygame.Rect(x, y, width, height)
        self.unpressed_img = unpressed_img
        self.pressed_img = pressed_img
        self.img = self.unpressed_img
        self.label = label

    def check_collision(self, mouse_pos):
        if self.rect.x<=mouse_pos[0]<=self.rect.width and self.rect.y<=mouse_pos[1]<=self.rect.height:
            print(f"Button '{self.label}' clicked!")
            game_mode=self.perform_action()
            return game_mode
        else:
            return None

    def perform_action(self):
        if self.label == 'menue_button':
            return 4
        if self.label == 'play_local_button':
            return 1
        if self.label == 'play_lan_button':
            return 2
        if self.label == 'score_button':
            return 3

    def draw(self, screen):
        screen.spiel_fenster.blit(self.img, self.rect)
        
