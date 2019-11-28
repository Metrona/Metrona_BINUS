#%%
import pygame
from pygame.sprite import Sprite
class paddle(Sprite):
    #paddle creation
    def __init__(self,game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        #getting paddle image
        self.image = pygame.image.load("Paddle.bmp")
        self.rect = self.image.get_rect()
        #positioning paddle in screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.y = 570
        #defining moving_right and left
        self.moving_right = False
        self.moving_left = False
        #setting default paddle speed
        self.paddle_speed = 0.9
        self.updating_paddle_speed = self.paddle_speed
        self.center = float(self.rect.centerx)
        
    def blitme(self):
        #creating image
        self.screen.blit(self.image, self.rect)

    def update(self):
        #moving paddle
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.center += self.updating_paddle_speed
        if self.moving_left and self.rect.left >= self.screen_rect.left:
            self.center -= self.updating_paddle_speed
        self.rect.centerx = self.center