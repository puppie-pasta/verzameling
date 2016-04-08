import pygame
import random

pygame.init()

wit = (255,255,255)
rood = (255,0,0)
zwart = (0,0,0)

screen = pygame.display.set_mode((1000,1000))
screen.fill(wit)

graden = 0

dagen = 1
maanden = 1
jaren = 0
schrikkeljaar = 0

tijd = 0

half_bewolkt_kans = random.randrange(1,200)
bewolkt_kans = random.randrange(1,200)
regen_kans = random.randrange(1,200)
onweerkans = random.randrange(1,200)

half_bewolkt_kans_zeker = 100
bewolkt_kans_zeker = 100
regen_kans_zeker = 100
onweerkans_zeker = 1

def onweer():
  onweer = pygame.image.load("onweer.png")
  screen.blit(onweer,[0,0])

def sneeuw():
  sneeuw = pygame.image.load("sneeuw.png")
  screen.blit(sneeuw,[0,0])

def regen():
  regen = pygame.image.load("regen.png")
  screen.blit(regen,[0,0])

def bewolkt():
  wolk = pygame.image.load("bewolkt.png")
  screen.blit(wolk,[0,0])

def half_zonnig():
  zon_bewolkt = pygame.image.load("half bewolkt.png")
  screen.blit(zon_bewolkt,[0,0])

def zonnig():
  zon = pygame.image.load("zon.png")
  screen.blit(zon,[0,0])

def jaar(jaren):
  font = pygame.font.SysFont(None,30)
  text = font.render("jaar"+str(jaren),True,zwart)
  screen.blit(text,[300,800])

def maand(maanden):
  font = pygame.font.SysFont(None,30)
  text = font.render("maand"+str(maanden),True,zwart)
  screen.blit(text,[200,800])

def dag(dagen):
  font = pygame.font.SysFont(None,30)
  text = font.render("dag"+str(dagen),True,zwart)
  screen.blit(text,[100,800])

def temperatuur(graden):
  font = pygame.font.SysFont(None,30)
  text = font.render("Co"+str(graden),True,rood)
  screen.blit(text,[100,100])

exit = False

while not exit:
  for event in pygame.event.get():
  	if event.type == pygame.KEYDOWN:
  	  if event.key == pygame.K_q:
  	  	exit = True

  tijd += 1

  screen.fill(wit)

  if half_bewolkt_kans <= half_bewolkt_kans_zeker:
  	half_zonnig()

  if bewolkt_kans <= bewolkt_kans_zeker:
  	bewolkt()

  if regen_kans <= regen_kans_zeker and graden < 0:
  	sneeuw()

  if regen_kans <= regen_kans_zeker and graden >= 0:
  	regen()

  if onweerkans <= onweerkans_zeker:
  	onweer()

  if half_bewolkt_kans > half_bewolkt_kans_zeker and bewolkt_kans > bewolkt_kans_zeker and regen_kans > regen_kans_zeker and onweerkans > onweerkans_zeker:
  	zonnig()

  if tijd == 15:
  	tijd = 0
  	dagen += 1
  	graden = random.randrange(-12,12)
  	half_bewolkt_kans = random.randrange(1,200)
  	bewolkt_kans = random.randrange(1,200)
  	regen_kans = random.randrange(1,200)
  	onweerkans = random.randrange(1,200)
  
  if graden >= 30:
  	onweerkans_zeker = 200
  if graden >= 25:
  	onweerkans_zeker = 190
  if graden >= 20:
  	onweerkans_zeker = 180
  if graden >= 15:
  	onweerkans_zeker = 80
  if graden >= 10:
  	onweerkans_zeker = 5

  if maanden == 1 and tijd == 0:
  	half_bewolkt_kans_zeker = 100
  	bewolkt_kans_zeker = 100
  	regen_kans_zeker = 100
  if maanden == 2 and tijd == 0:
  	half_bewolkt_kans_zeker = 100
  	bewolkt_kans_zeker = 100
  	regen_kans_zeker = 100
  if maanden == 3 and tijd == 0:
  	half_bewolkt_kans_zeker = 100
  	bewolkt_kans_zeker = 70
  	regen_kans_zeker = 40
  if maanden == 4 and tijd == 0:
  	half_bewolkt_kans_zeker = 80
  	bewolkt_kans_zeker = 50
  	regen_kans_zeker = 30
  if maanden == 5 and tijd == 0:
  	half_bewolkt_kans_zeker = 80
  	bewolkt_kans_zeker = 40
  	regen_kans_zeker = 30
  if maanden == 6 and tijd == 0:
  	half_bewolkt_kans_zeker = 50
  	bewolkt_kans_zeker = 30
  	regen_kans_zeker = 20
  if maanden == 7 and tijd == 0:
  	half_bewolkt_kans_zeker = 50
  	bewolkt_kans_zeker = 30
  	regen_kans_zeker = 20
  if maanden == 8 and tijd == 0:
  	half_bewolkt_kans_zeker = 50
  	bewolkt_kans_zeker = 30
  	regen_kans_zeker = 20
  if maanden == 9 and tijd == 0:
  	half_bewolkt_kans_zeker = 40
  	bewolkt_kans_zeker = 80
  	regen_kans_zeker = 120
  if maanden == 10 and tijd == 0:
  	half_bewolkt_kans_zeker = 20
  	bewolkt_kans_zeker = 60
  	regen_kans_zeker = 170
  if maanden == 11 and tijd == 0:
  	half_bewolkt_kans_zeker = 20
  	bewolkt_kans_zeker = 60
  	regen_kans_zeker = 170
  if maanden == 12 and tijd == 0:
  	half_bewolkt_kans_zeker = 100
  	bewolkt_kans_zeker = 100
  	regen_kans_zeker = 100

  if maanden == 1 and tijd == 0:
  	graden = random.randrange(-12,12)
  if maanden == 2 and tijd == 0:
  	graden = random.randrange(-10,13)
  if maanden == 3 and tijd == 0:
  	graden = random.randrange(-3,18)
  if maanden == 4 and tijd == 0:
  	graden = random.randrange(5,23)
  if maanden == 5 and tijd == 0:
  	graden = random.randrange(10,26)
  if maanden == 6 and tijd == 0:
  	graden = random.randrange(15,32)
  if maanden == 7 and tijd == 0:
  	graden = random.randrange(15,33)
  if maanden == 8 and tijd == 0:
  	graden = random.randrange(15,33)
  if maanden == 9 and tijd == 0:
  	graden = random.randrange(10,26)
  if maanden == 10 and tijd == 0:
  	graden = random.randrange(5,23)
  if maanden == 11 and tijd == 0:
  	graden = random.randrange(-3,18)
  if maanden == 12 and tijd == 0:
  	graden = random.randrange(-12,12)

  if dagen > 31 and maanden == 1:
  	dagen = 1
  	maanden = 2
  if dagen > 29 and maanden == 2 and schrikkeljaar == 0:
  	dagen = 1
  	maanden = 3
  if dagen > 28 and maanden == 2 and schrikkeljaar > 0:
  	dagen = 1
  	maanden = 3
  if dagen > 31 and maanden == 3:
  	dagen = 1
  	maanden = 4
  if dagen > 30 and maanden == 4:
  	dagen = 1
  	maanden = 5
  if dagen > 31 and maanden == 5:
  	dagen = 1
  	maanden = 6
  if dagen > 30 and maanden == 6:
  	dagen = 1
  	maanden = 7
  if dagen > 31 and maanden == 7:
  	dagen = 1
  	maanden = 8
  if dagen > 31 and maanden == 8:
  	dagen = 1
  	maanden = 9
  if dagen > 30 and maanden == 9:
  	dagen = 1
  	maanden = 10
  if dagen > 31 and maanden == 10:
  	dagen = 1
  	maanden = 11
  if dagen > 30 and maanden == 11:
  	dagen = 1
  	maanden = 12
  if dagen > 31 and maanden == 12:
  	dagen = 1
  	maanden = 1
  	jaren += 1
  	schrikkeljaar += 1

  if schrikkeljaar == 4:
  	schrikkeljaar = 0

  temperatuur(graden)
  dag(dagen)
  maand(maanden)
  jaar(jaren)
  pygame.display.update()