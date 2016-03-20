import pygame
import random

pygame.init()

groen = (0,255,0)
geel = (255,255,0)
zwart = (0,0,0)
wit = (255,255,255)
grijs = (200,200,200)

screen = pygame.display.set_mode((1000,1000))
screen.fill(groen)

x_rechterbaan = 500
y_rechterbaan = -500

x_linkerbaan = 400
y_linkerbaan = -500
y_wegstreep_speed = 0

x_wegstreep = 500
y_wegstreep = 500

x_auto = 550
y_auto = 500
x_auto_speed = 0

aantal_snelheid = 0

x_halte = 600
y_halte = random.randrange(-9000,-1000)
y_halte_speed = 0

geld = 100

halte_tijd = 0

flitspaal_tijd = 0

x_flitspaal = 600
y_flitspaal = random.randrange(-9000,-1000)
y_flitspaal_speed = 0

def flitspaal(x_flitspaal,y_flitspaal):
  pygame.draw.rect(screen,grijs,[x_flitspaal,y_flitspaal,60,60])

def jouwgeld(geld):
  font = pygame.font.SysFont(None,50)
  text = font.render("geld:"+str(geld),True,wit)
  screen.blit(text,[100,800])

def halte(x_halte,y_halte):
  pygame.draw.rect(screen,zwart,[x_halte,y_halte,100,500])

def snelheid(aantal_snelheid):
  font = pygame.font.SysFont(None,50)
  text = font.render("snelheid"+str(aantal_snelheid),True,wit)
  screen.blit(text,[100,100])

def linkerbaan(x_linkerbaan,y_linkerbaan):
  pygame.draw.rect(screen,zwart,[x_linkerbaan,y_linkerbaan,100,10000])

def wegstreep(x_wegstreep,y_wegstreep):
  pygame.draw.rect(screen,wit,[x_wegstreep,y_wegstreep,3,300])

def rechterbaan(x_rechterbaan,y_rechterbaan):
  pygame.draw.rect(screen,zwart,[x_rechterbaan,y_rechterbaan,100,10000])

def auto(x_auto,y_auto):
  pygame.draw.circle(screen,geel,[x_auto,y_auto],30)

exit = False

while not exit:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q:
        exit = True
      if event.key == pygame.K_UP:
        y_wegstreep_speed -= 1
        aantal_snelheid -= 10
        y_halte_speed -= 1
        y_flitspaal_speed -= 1
      if event.key == pygame.K_DOWN:
        y_wegstreep_speed += 1
        aantal_snelheid += 10
        y_halte_speed += 1
        y_flitspaal_speed += 1
      if event.key == pygame.K_RIGHT:
        x_auto_speed += 1
      if event.key == pygame.K_LEFT:
        x_auto_speed -= 1

  screen.fill(groen)      

  if y_wegstreep > 1000:
    y_wegstreep = 0

  if y_halte+500 > y_auto > y_halte and aantal_snelheid == 0 and halte_tijd == 0:
    geld += 10
    halte_tijd += 1
    y_halte = random.randrange(-9000,-1000)

  if halte_tijd == 1:
    halte_tijd = 0

  if y_flitspaal+50 > y_auto > y_flitspaal and aantal_snelheid > 50 and flitspaal_tijd == 0:
    geld -= 10
    flitspaal_tijd += 1 
    y_flitspaal = random.randrange(-9000,-1000)

  if y_flitspaal > 1000:
    y_flitspaal = random.randrange(-9000,-1000)  

  if flitspaal_tijd == 1:
    flitspaal_tijd = 0

  if geld <= 0:
    exit = True                

  y_wegstreep += y_wegstreep_speed
  x_auto += x_auto_speed
  y_halte += y_halte_speed
  y_flitspaal += y_flitspaal_speed          
  
  rechterbaan(x_rechterbaan,y_rechterbaan)
  linkerbaan(x_linkerbaan,y_linkerbaan)
  wegstreep(x_wegstreep,y_wegstreep)
  auto(x_auto,y_auto)
  snelheid(aantal_snelheid)
  halte(x_halte,y_halte)
  jouwgeld(geld)
  flitspaal(x_flitspaal,y_flitspaal)
  pygame.display.update()
