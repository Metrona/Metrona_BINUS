#%%
import pygame
from pygame.sprite import Sprite

class block(Sprite):
    def __init__(self,game):
        super(block, self).__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        #getting paddle image
        self.image = pygame.image.load("Block.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
    def blitme(self):
        #creating image
        self.screen.blit(self.image, self.rect)
