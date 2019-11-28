#%%
import pygame, sys
from Paddle import paddle
from Ball import ball
from Block import block
from pygame.sprite import Group
import Blockcreation as b

class MainGame:
    #intialization for main game
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        self.Paddle = paddle(self)
        self.Block = block(self)
        self.blocks = Group()
        self.balls = Group()
        self.scorefont = pygame.font.SysFont("monospace", 16)
        self.gameoverfont = pygame.font.SysFont("monospace", 120)
        self.highscorefont = pygame.font.SysFont("monospace", 30)
        self.score = 0
        with open("highscore.txt") as f:
            contents = f.read()
        self.high = int(contents)
        b.create_wall(self, self.blocks)
        self.Ball = ball(self, self.Paddle, self.blocks)
        self.balls.add(self.Ball)
        self.game_over = False
        self.pause = False
        
    #event checker
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #checking what key is held down
            elif event.type == pygame.KEYDOWN:
                if self.pause == False:
                    if event.key == pygame.K_RIGHT:
                        #changing to True so if function in paddle works
                        self.Paddle.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.Paddle.moving_left = True
                    elif event.key == pygame.K_ESCAPE and self.game_over == False:
                        self.Paddle.moving_left = False
                        self.Paddle.moving_right = False
                        self.pause = True
                    elif event.key == pygame.K_SPACE and self.game_over == False:
                        self.Ball.release()
                    elif event.key == pygame.K_SPACE and self.game_over == True:
                        start_game()
                elif self.pause == True:
                    if event.key == pygame.K_ESCAPE:
                        self.pause = False
                    elif event.key == pygame.K_q:
                        sys.exit()
                        
            #checking if released
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    #changing to False to stop if function in paddle
                    self.Paddle.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.Paddle.moving_left = False
                    
    def scoreupdate(self):
        scoretext = self.scorefont.render("Score {0}".format(self.score), True, (255,255,255))
        self.screen.blit(scoretext, (5, 10))
        
    def gameover(self):
        if self.Ball.rect.y >= 620:
            self.Ball.kill()
        if len(self.balls) == 0:
            Gameovertext = self.gameoverfont.render("Game Over", True, (255,255,255))
            self.screen.blit(Gameovertext, (80, 180))
            if self.score < self.high:
                highscoretext = self.highscorefont.render("Highscore: " + str(self.high), True, (255,255,255))
                self.screen.blit(highscoretext, (250, 320))
            elif self.score >= self.high:
                highscoretext = self.highscorefont.render("New Highscore: " + str(self.score), True, (255,255,255))
                self.screen.blit(highscoretext, (220, 320))
                with open("highscore.txt", 'w') as f:
                    f.write(str(self.score))
            self.game_over = True
            
    def next_round(self):
        if len(self.blocks) == 0:
            b.create_wall(self, self.blocks)
            ball.new_values(self.Ball)
                
    def _update_screen(self):
        #colour filler
        self.screen.fill((0,0,0))
        #creating image on screen
        self.Paddle.blitme()
        self.Ball.blitme()
        self.scoreupdate()
        self.blocks.draw(self.screen)
        self.gameover()
        if self.pause == True:
            pausetext = self.gameoverfont.render("Paused", True, (255,255,255))
            self.screen.blit(pausetext, (180, 180))
            pauseinst = self.highscorefont.render("Press q to quit or esc to continue", True, (255,255,255))
            self.screen.blit(pauseinst, (100, 320))
        self.next_round()
        pygame.display.flip()
                
    def run_game(self):
        while self.game_over == False:
            self.Paddle.update()
            if self.pause == False:
                self.Ball.update()
            self._update_screen()
            self._check_events()
        while self.game_over == True:
            self._check_events()
                        
def start_game():           
    if __name__ == "__main__":
        mg = MainGame()
        mg.run_game()
start_game()