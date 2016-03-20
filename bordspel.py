import pygame

pygame.init()

wit = (255,255,255)
zwart = (0,0,0)

screen = pygame.display.set_mode((1000,1000))
screen.fill(wit)

x_rond = 500
y_rond = 100

def rond(x_rond,y_rond):
  pygame.draw.circle(screen,zwart,[x_rond,y_rond],50)

exit = False

while not exit:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q:
        exit = True                    	

  screen.fill(wit)
  rond(x_rond,y_rond)
  pygame.display.update()