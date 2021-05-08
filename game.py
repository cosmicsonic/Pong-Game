import pygame
import random
from ball import Ball
from paddle import Paddle
from powerdown import PowerDown
from player_input import PlayerInput
from datetime import datetime

class Game:
  def __init__(self):
    self.screen_width = 640
    self.screen_height = 480
    self.size = (self.screen_width, self.screen_height)
    self.screen = pygame.display.set_mode(self.size)
    self.ball = Ball(60,60, 25)
    self.paddle = Paddle(25,0,25,100)
    self.score = 0
    self.player_input = PlayerInput()

    invisible = PowerDown(100, 100,self.makePaddleInvisible, self.makePaddleVisible, 5, (0,0,255))
    shrink = PowerDown(200,200, self.shrinkPaddle,self.expandPaddle,5,(255,0,0))
    self.powerdowns = [shrink, invisible]
    shrink.is_active = True
    self.active = [shrink]
    self.running = []
    self.random_time = 10

    self.powerdown_last = None

  def checkHitPowerDowns(self):
    for pd in self.active:
      if self.ball.collidePowerDown(pd):
        current_powerdown = pd
        current_powerdown.runEffect()
        self.active.remove(pd)
        self.running.append(pd)
  
  def checkToRemovePowerDown(self):
    for pd in self.running:
      if not pd.is_running():
        pd.undo()
        self.running.remove(pd)
        self.powerdown_last = datetime.now()

  def drawPowerdowns(self):
    for pd in self.active:
      pd.draw(self.screen)

  def makePaddleInvisible(self):
    self.paddle.color = (0,0,0)

  def makePaddleVisible(self):
    self.paddle.color = (0,255,0)

  def shrinkPaddle(self):
    self.paddle.height = 20

  def expandPaddle(self):
    self.paddle.height = 100
  
  def checkActivatePowerDown(self):
    if self.powerdown_last != None:
      now = datetime.now()
      if now.second > self.powerdown_last.second + self.random_time:
        self.randome_time = random.randint(5,20)
        self.activatePowerDown()

  def activatePowerDown(self):
    self.powerdown_last = None
    pd = random.choice(self.powerdowns)
    pd.x = random.randint(50,600)
    pd.y = random.randint(50,400)
    pd.is_active = True
    self.active.append(pd)

  def displayText(self, text, x, y):
    black = (0,0,0)
    white = (255,255,255)
    font = pygame.font.SysFont("Comic Sans", 64)
    display_text = font.render(text, True, white, black)
    display_rect = display_text.get_rect()
    display_rect.center = (x, y)
    self.screen.blit(display_text, display_rect)

  def checkBallHitPaddle(self):
    if self.ball.collidePaddle(self.paddle):
      self.ball.x_direction = "right"
      self.ball.speed += 0.1
      self.score += 1
    
    if self.ball.collide_with_top:
      self.ball.y_direction = 'up'
    elif self.ball.collide_with_bottom:
      self.ball.y_direction = 'down'

  def checkMiss(self):
    if self.ball.x < 0:
      self.ball.speed = 1
      self.score = 0
      self.random_time = 10

  def getInput(self, event, is_enabled):
    if event.key == pygame.K_UP:
      self.player_input.up = is_enabled
    if event.key == pygame.K_DOWN:
      self.player_input.down = is_enabled

  def handleInput(self):
    if self.player_input.up == True and self.paddle.getCenter() >= 0:
      self.paddle.y -= self.paddle.speed
    
    if self.player_input.down == True and self.paddle.getCenter() <= self.screen_height:
      self.paddle.y += self.paddle.speed

  def draw(self):
    self.screen.fill((0,0,0))
    self.ball.draw(self.screen)
    self.paddle.draw(self.screen)
    self.displayText(str(self.score), self.screen_width/2, 25)
  
  def run(self):
    self.draw()
    self.checkToRemovePowerDown()   
    self.ball.move()
    self.handleInput()
    self.drawPowerdowns()
    self.checkHitPowerDowns()
    self.checkBallHitPaddle()
    self.checkMiss()
    self.checkActivatePowerDown()
