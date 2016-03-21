import pygame
import random

pygame.init()

groen = (0,255,0)
licht_blauw = (0,255,255)
geel = (255,255,0)
wit = (255,255,255)
zwart = (0,0,0)

screen = pygame.display.set_mode((1000,1000))
screen.fill(licht_blauw)

x_gras = 0
y_gras = 900

x_zon = 500
y_zon = 100

datum = 1
maand = 1
jaar = 0

tijd = 0

temperatuur = random.randrange(-12,12)

def display_temperatuur(temperatuur):
  font = pygame.font.SysFont(None,50)
  text = font.render("Co"+str(temperatuur),True,zwart)
  screen.blit(text,[100,100])


def tijd_datum(jaar):
  font = pygame.font.SysFont(None,50)
  text = font.render(str(jaar),True,wit)
  screen.blit(text,[850,100])

def tijd_maand(maand):
  font = pygame.font.SysFont(None,50)
  text = font.render(str(maand),True,wit)
  screen.blit(text,[900,100])

def tijd_jaar(datum):
  font = pygame.font.SysFont(None,50)
  text = font.render(str(datum),True,wit)
  screen.blit(text,[950,100])


def zon(x_zon,y_zon):
  pygame.draw.circle(screen,geel,[x_zon,y_zon],50)

def gras(x_gras,y_gras):
  pygame.draw.rect(screen,groen,[x_gras,y_gras,1000,100])

exit = False

while not exit:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q:
        exit = True
  
  screen.fill(licht_blauw)

  tijd += 1

  if tijd == 100:
    tijd = 0
    datum += 1
    temperatuur = random.randrange(-12,12)
    if maand < 2:
      temperatuur = random.randrange(-10,13)
    if maand == 2 and datum >= 21:
      temperatuur = random.randrange(-7,15)
    if maand == 3 and datum < 11:
      temperatuur = random.randrange(-5,16)
    if maand == 3 and datum < 21:
      temperatuur = random.randrange(-4,18)
    if maand < 4 and datum >= 21:
      temperatuur = random.randrange(-3,19)
    if maand == 4 and datum < 11:
      temperatuur = random.randrange(-2,21)
    if maand == 4 and datum < 21:
      temperatuur = random.randrange(0,22)
    if maand < 5 and datum >= 21:
      temperatuur = random.randrange(3,25)
    if maand == 5 and datum < 11:
      temperatuur = random.randrange(6,26)
    if maand == 5 and datum < 21:
      temperatuur = random.randrange(8,28)
    if maand < 6 and datum >= 21:
      temperatuur = random.randrange(10,29)
    if maand == 6 and datum < 21:
      temperatuur = random.randrange(11,31)
    if maand < 7 and datum >= 21:
      temperatuur = random.randrange(12,32)
    if maand == 7:
      temperatuur = random.randrange(13,33)
    if maand == 8 and datum < 21:
      temperatuur = random.randrange(12,32)
    if maand == 8 and datum >= 21:
      temperatuur = random.randrange(11,31)
    if maand < 9 and datum >= 21:
      temperatuur = random.randrange(11,30)
    if maand == 9 and datum < 11:
      temperatuur = random.randrange(10,28)
    if maand == 9 and datum < 21:
      temperatuur = random.randrange(8,26)
    if maand < 10 and datum >= 21:
      temperatuur = random.randrange(6,24)
    if maand == 10 and datum < 11:
      temperatuur = random.randrange(5,23)
    if maand == 10 and datum < 21:
      temperatuur = random.randrange(4,22)
    if maand < 11 and datum >= 21:
      temperatuur = random.randrange(2,20)
    if maand == 11 and datum < 11:
      temperatuur = random.randrange(0,19)
    if maand == 11 and datum < 21:
      temperatuur = random.randrange(-5,16)
    if maand < 12 and datum >= 21:
      temperatuur = random.randrange(-7,13)
    if maand == 12 and datum < 11:
      temperatuur = random.randrange(-10,12)
    if maand == 12 and datum < 21:
      temperatuur = random.randrange(-13,11)
    if maand == 12 and datum >= 21:
      temperatuur = random.randrange(-12,12)                
                                    

  if datum > 31 and maand == 1:
    datum = 1
    maand += 1

  if datum > 28 and maand == 2:
    datum = 1
    maand += 1

  if datum > 31 and maand == 3:
    datum = 1
    maand += 1

  if datum > 30 and maand == 4:
    datum = 1
    maand += 1

  if datum > 31 and maand == 5:
    datum = 1
    maand += 1

  if datum > 30 and maand == 6:
    datum = 1
    maand += 1

  if datum > 31 and maand == 7:
    datum = 1
    maand += 1

  if datum > 31 and maand == 8:
    datum = 1
    maand += 1

  if datum > 30 and maand == 9:
    datum = 1
    maand += 1

  if datum > 31 and maand == 10:
    datum = 1
    maand += 1

  if datum > 30 and maand == 11:
    datum = 1
    maand += 1

  if datum > 31 and maand == 12:
    datum = 1
    maand += 1
    jaar += 1
  
  
  zon(x_zon,y_zon)
  gras(x_gras,y_gras)
  tijd_datum(jaar)
  tijd_maand(maand)
  tijd_jaar(datum)
  display_temperatuur(temperatuur)
  pygame.display.update()