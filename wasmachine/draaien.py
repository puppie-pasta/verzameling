import pygame
import pygame.locals

white = (255, 255, 255)

pygame.init()

display = pygame.display.set_mode((300, 300))
fpsClock = pygame.time.Clock()

image = pygame.image.load('w.jpg')
draai = 1400

ecit = False

while 1:


    display.fill(white)

    draai = 1

    image = pygame.transform.rotate(image, draai)
    rect = image.get_rect()
    rect.center = (150,150)

    display.blit(image, rect)

    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          exit = True


    pygame.display.update()
    fpsClock.tick(60)
