import pygame
from game import Game

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
done = False

game = Game()

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.KEYDOWN:
      game.getInput(event, True)
    if event.type == pygame.KEYUP:
      game.getInput(event, False)

  game.run()

  pygame.display.flip()
  clock.tick(250)