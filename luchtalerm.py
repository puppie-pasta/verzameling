import pygame

pygame.init()

wit = (255,255,255)
zwart = (0,0,0)
rood = (255,0,0)

screen = pygame.display.set_mode((800,600))
screen.fill(wit)

x1 = 0
y1 = 0
x2 = 400
y2 = 300
x1_speed = 0
y1_speed = 0

def luchtalerm(x2,y2):
    pygame.draw.circle(screen,rood,[x2,y2],40)
    pygame.display.update()

def bron(x1,y1):
    pygame.draw.circle(screen,zwart,[x1,y1],20)
    pygame.display.update()

luchtsirene = pygame.mixer.Sound("Luchtalarm (1).wav")
pygame.mixer.Sound.play(luchtsirene)
 

while 1:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        x1 += 10
      if event.key == pygame.K_LEFT:
        x1 -= 10
      if event.key == pygame.K_DOWN:
        y1 += 10
      if event.key == pygame.K_UP:
        y1 -= 10      
                          
  bron(x1,y1)
  luchtalerm(x2,y2)
  x1 += x1_speed
  y1 += y1_speed
  screen.fill(wit)
  
    
