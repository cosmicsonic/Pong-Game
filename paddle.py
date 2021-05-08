import pygame

class Paddle:
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = (0,255,0)
    self.speed = 1
  
  def getTopRect(self):
    return pygame.Rect(self.x, self.y, self.width, self.height//2)
  
  def getBottomRect(self):
    return pygame.Rect(self.x, self.y+self.height//2, self.width, self.height//2)
  
  def move(self, pos):
    self.y = pos[1] - self.height / 2
  
  def draw(self, screen):
    top_rect = self.getTopRect()
    bottom_rect = self.getBottomRect()
    pygame.draw.rect(screen, self.color, top_rect)
    pygame.draw.rect(screen, self.color, bottom_rect)
  
  def getCenter(self):
    return self.y + (self.height / 2)