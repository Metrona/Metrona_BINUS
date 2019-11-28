#%%
import pygame
from pygame.sprite import Sprite
class ball(Sprite):
    #paddle creation
    def __init__(self,game,spaddle, gblock):
        super(ball, self).__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.paddle = spaddle
        self.blocks = gblock
        self.game = game
        #getting ball image
        self.image = pygame.image.load("Ball.bmp")
        self.rect = self.image.get_rect()
        #positioning ball in screen
        self.y = float(self.rect.y)
        self.x = float(self.rect.y)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.paddle.rect.top
        self.default_ball_speed = 1
        self.updating_ball_speed = self.default_ball_speed
        self.scoreround = 100
        self.default_state = True
        self.upr = False
        self.upl = False
        self.downr = False
        self.downl = False
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        
    def release(self):
        if self.default_state == True:
            if self.paddle.moving_left == True:
                self.upl = True
            else:
                self.upr = True
            self.default_state = False
    
    def new_values(self):
        self.scoreround += 100
        self.updating_ball_speed += 0.1
        self.paddle.updating_paddle_speed += 0.1
        
    def update(self):
        self.col = pygame.sprite.collide_rect(self, self.paddle)
        self.broke = pygame.sprite.groupcollide(self.game.balls, self.blocks, False, True)
        
        if self.default_state == True and self.paddle.rect.right <= self.screen_rect.right and self.paddle.rect.left >= self.screen_rect.left and self.paddle.moving_right:
            self.x += self.paddle.paddle_speed
        if self.default_state == True and self.paddle.rect.right <= self.screen_rect.right and self.paddle.rect.left >= self.screen_rect.left and self.paddle.moving_left:
            self.x -= self.paddle.paddle_speed
            
        if self.rect.right >= self.screen_rect.right and self.upr == True:
            self.upr = False
            self.upl = True
        elif self.rect.right >= self.screen_rect.right and self.downr == True:
            self.downr = False
            self.downl = True
        elif self.rect.left <= self.screen_rect.left and self.upl == True:
            self.upl = False
            self.upr = True
        elif self.rect.left <= self.screen_rect.left and self.downl == True:
            self.downr = True
            self.downl = False
        elif self.rect.top <= self.screen_rect.top and self.upr == True:
            self.downr = True
            self.upr = False
        elif self.rect.top <= self.screen_rect.top and self.upl == True:
            self.downl = True
            self.upl = False
        elif self.col == True and self.downl:
            self.downl = False
            self.upl = True
        elif self.col == True and self.downr:
            self.downr = False
            self.upr = True
        elif self.broke and self.upl:
            self.downl = True
            self.upl = False
            self.game.score += self.scoreround
        elif self.broke and self.upr:
            self.downr = True
            self.upr = False
            self.game.score += self.scoreround
        elif self.broke and self.downl:
            self.downl = False
            self.upl = True
            self.game.score += self.scoreround
        elif self.broke and self.downr:
            self.downr = False
            self.upr = True
            self.game.score += self.scoreround
        
        if self.upr == True:
            self.y -= self.updating_ball_speed
            self.x += self.updating_ball_speed
        elif self.upl == True:
            self.y -= self.updating_ball_speed
            self.x -= self.updating_ball_speed
        elif self.downr == True:
            self.y += self.updating_ball_speed
            self.x += self.updating_ball_speed
        elif self.downl == True:
            self.y += self.updating_ball_speed
            self.x -= self.updating_ball_speed
        self.rect.y = self.y
        self.rect.x = self.x
        
        
    def blitme(self):
        #creating image
        self.screen.blit(self.image, self.rect)
