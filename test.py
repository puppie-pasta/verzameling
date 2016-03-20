import pygame

pygame.init()

wit = (255,255,255)

screen = pygame.display.set_mode((1000,1000))
screen.fill(wit)

exit = False

while not exit:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q:
        exit = True

  pygame.display.update()