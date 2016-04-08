import pygame

pygame.init()

wit = (255,255,255)

screen = pygame.display.set_mode((500,500))

foto = pygame.image.load("w.jpg")
screen.blit(foto,[0,0])
draai_foto = pygame.rotate(foto,1)

exit = False

while not exit:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q:
        exit = True      
  
  foto
  pygame.display.update()