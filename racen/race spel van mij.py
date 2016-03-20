import pygame
import random

pygame.init()

wit = (255,255,255)
groen = (0,255,0)
rood = (255,0,0)
zwart = (0,0,0)
oranje = (255,100,0)

screen = pygame.display.set_mode((1000,1000))
screen.fill(wit)

x_auto = 500
y_auto = 500
x_auto_speed = 0

x_blok = random.randrange(0,900)
y_blok = 0
y_blok_speed = 0

aantal_score = 0

def score(aantal_score):
  font = pygame.font.SysFont(None,50)
  text = font.render("score:"+str(aantal_score),True,zwart)
  screen.blit(text,[50,50])

def blok(x_blok,y_blok):
  pygame.draw.rect(screen,rood,[x_blok,y_blok,200,200])

def auto(x_auto,y_auto):
  pygame.draw.circle(screen,oranje,[x_auto,y_auto],50)

exit = False

while not exit:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q:
        exit = True
      if event.key == pygame.K_UP:
        y_blok_speed += 1
      if event.key == pygame.K_DOWN:
        y_blok_speed -= 1
      if event.key == pygame.K_RIGHT:
        x_auto_speed += 1
      if event.key == pygame.K_LEFT:
        x_auto_speed -= 1          
  
  y_blok += y_blok_speed
  x_auto += x_auto_speed

  if y_blok > 1000:
    y_blok = 0
    x_blok = random.randrange(0,900)     

  screen.fill(wit)  

  if x_blok+200 > x_auto > x_blok and y_blok+200 > y_auto > y_blok:
    exit = True

  if x_blok+200 != x_auto and y_blok == x_auto:
    aantal_score += 1   

  score(aantal_score)
  auto(x_auto,y_auto)
  blok(x_blok,y_blok)
  pygame.display.update()