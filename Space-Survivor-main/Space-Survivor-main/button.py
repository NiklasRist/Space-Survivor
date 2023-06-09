import sys
import pygame

class button():

    '''def __init__(self, x, y, image, image_pressed, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.image_pressed = pygame.transform.scale(image_pressed, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
		#get mouse position
        pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

		#draw button on screen
        if self.clicked:
            surface.blit(self.image_pressed, (self.rect.x, self.rect.y))
        else:
            surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
    '''    

    def __init__(self, x, y, width, height, unpressed_img, pressed_img, label):
        self.rect = pygame.Rect(x, y, width, height)
        self.unpressed_img = pygame.image.load(unpressed_img)
        self.pressed_img = pygame.image.load(pressed_img)
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
        screen.blit(self.img, self.rect)
    