import pygame
from datetime import datetime

class PowerDown:  
  def __init__(self, x, y, effect, undo_effect, timeout, color):
    self.x = x
    self.y = y
    self.effect = effect
    self.size = 50
    self.color = color
    self.start_time = None
    self.timeout = timeout
    self.undo_effect = undo_effect
    self.is_active = False
  
  def getRect(self):
    return pygame.Rect(self.x,self.y,self.size,self.size)

  def draw(self, screen):
    rect = self.getRect()
    pygame.draw.rect(screen, self.color, rect)

  def is_running(self):
    now = datetime.now()
    elapsed = (now - self.start_time).seconds
    print(elapsed)
    return elapsed <= self.timeout

  def runEffect(self):
    self.start_time = datetime.now()
    self.effect()

  def undo(self):
    self.is_active = False
    self.start_time = None
    self.undo_effect()
  
