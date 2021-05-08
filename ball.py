import pygame

class Ball:
  def __init__(self, x, y, size):
    self.x = x
    self.y = y
    self.size = size
    self.x_direction = "right"
    self.y_direction = "down"
    self.speed = 1

    self.collide_with_top = False
    self.collide_with_bottom = False
  
  def move(self):
    if self.x_direction == "right":
      self.x += self.speed
    elif self.x_direction == "left":
      self.x -= self.speed
    
    if self.y_direction == "down":
      self.y += self.speed
    elif self.y_direction == "up":
      self.y -= self.speed
  
  def getRect(self):
    return pygame.Rect(self.x, self.y, self.size, self.size)
  
  def collidePaddle(self, paddle):
    ball_rect = self.getRect()
    paddle_top_rect = paddle.getTopRect()
    paddle_bottom_rect = paddle.getBottomRect()
    self.collide_with_top = ball_rect.colliderect(paddle_top_rect)
    self.collide_with_bottom = ball_rect.colliderect(paddle_bottom_rect)
    collide_paddle = self.collide_with_top or self.collide_with_bottom

    return collide_paddle and self.x_direction == "left"

  def collidePowerDown(self, pd):
    pd_rect = pd.getRect()
    ball_rect = self.getRect()

    return ball_rect.colliderect(pd_rect)

  def changeDirection(self, width, height):
    if self.x > width-self.size:
      self.x_direction = "left"
    if self.x < 0:
      self.x_direction = "right"
    
    if self.y > height-self.size:
      self.y_direction = "up"
    if self.y < 0:
      self.y_direction = "down"

  def draw(self, screen):
    width, height = pygame.display.get_window_size()
    self.changeDirection(width, height)
    rect = self.getRect()
    pygame.draw.rect(screen, (0,0,255), rect)