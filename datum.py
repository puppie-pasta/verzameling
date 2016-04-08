import pygame
import time
import random

pygame.init()

zwart = (0,0,0)
wit = (255,255,255)
oranje = (156,83,1)

screen = pygame.display.set_mode((770,590))
screen.fill(wit)

dagen = 1
maanden = 1
jaren = 0
schrikkeljaar = 0
tijddagen = 0
afgestoken = 0
graden = 0
uren = 0
mens_groote = float(50.0)
maanlicht = 0
uur = 0
minuten = 0
uur2 = 0
minuten2 = 0

global dagnummer
dagnummer = 1

def dagnaam(nummer):
  if nummer == 1:
    return "zondag"
  if nummer == 2:
    return "maandag"
  if nummer == 3:
    return "dinsdag"
  if nummer == 4:
    return "woensdag"
  if nummer == 5:
    return "donderdag"
  if nummer == 6:
    return "vrijdag"
  if nummer == 7:
    return "zaterdag"

def schrikkeljaar(huidigjaar):
  if (huidigjaar % 4) == 0:
    if (huidigjaar % 100) == 0:
      if (huidigjaar % 400) == 0:
        return 1
      else:
        return 0
    else:
      return 1
  else:
    return 0

def tijd_minuten2(minuten2):
  font = pygame.font.SysFont(None,40)
  text = font.render(":"+str(minuten),True,zwart)
  screen.blit(text,[150,400])

def tijd_uur2(uur2):
  font = pygame.font.SysFont(None,40)
  text = font.render(("zonsondergang")+str(uur2),True,zwart)
  screen.blit(text,[100,400])

def tijd_minuten(minuten):
  font = pygame.font.SysFont(None,40)
  text = font.render(":"+str(minuten),True,zwart)
  screen.blit(text,[150,500])

def tijd_uur(uur):
  font = pygame.font.SysFont(None,40)
  text = font.render(("zonsopkomst")+str(uur),True,zwart)
  screen.blit(text,[100,500])

def maanface(maanlicht):
  font = pygame.font.SysFont(None,40)
  text = font.render(("De maanface is")+str(maanlicht),True,zwart)
  screen.blit(text,[300,500])

def temperatuur(graden):
  font = pygame.font.SysFont(None,40)
  text = font.render(("De maximaal temperatuur is  ")+str(graden),True,zwart)
  screen.blit(text,[100,500])

def vuurwerk(afgestoken):
  font = pygame.font.SysFont(None,40)
  text = font.render(("De hoeveelheid vuurwerk dat werd afgestoken is")+str(afgestoken),True,zwart)
  screen.blit(text,[0,400])


def afsluittekst():
  font = pygame.font.SysFont(None,40)
  text = font.render(("Druk op 'Q' om af te sluiten"),True,oranje)
  screen.blit(text,[10,10])

def jaar(jaren):
  getal = pygame.font.SysFont(None,50)
  bijschrift = pygame.font.SysFont(None,30)

  getaltext = getal.render(str(jaren).zfill(4),True,zwart)
  bijschrifttext = bijschrift.render(("Jaar"),True,zwart)

  screen.blit(getaltext,[440,300])
  screen.blit(bijschrifttext,[455,350])

def maand(maanden):
  getal = pygame.font.SysFont(None,50)
  bijschrift = pygame.font.SysFont(None,30)

  getaltext = getal.render(str(maanden).zfill(2),True,zwart)
  bijschrifttext = bijschrift.render(("Maand"),True,zwart)

  screen.blit(getaltext,[350,300])
  screen.blit(bijschrifttext,[338,350])

def dag(dagen, speciaal = 0):
  getal = pygame.font.SysFont(None,50)
  bijschrift = pygame.font.SysFont(None,30)
  naampje = pygame.font.SysFont(None,80)

  getaltext = getal.render(str(dagen).zfill(2),True,zwart)
  bijschrifttext = bijschrift.render(("Dag"),True,zwart)
  naampjetext = naampje.render((dagnaam(dagnummer)),True,zwart)

  screen.blit(getaltext,[250,300])
  screen.blit(bijschrifttext,[250,350])
  screen.blit(naampjetext,[250,200])

pygame.quit = False

while not pygame.quit:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_s:
        dag(dagen)
        dagen += 1
        dagnummer += 1
        if dagen >= 1 and maanden >= 10:
          afgestoken = random.randrange(0,1)
        if dagen >= 1 and maanden >= 11:
          afgestoken = random.randrange(1,3)
        if dagen >= 21 and maanden >= 11:
          afgestoken = random.randrange(1,3)
        if dagen >= 21 and maanden >= 12:
          afgestoken = random.randrange(1,5)
        if dagen >= 29 and maanden >= 12:
          afgestoken += random.randrange(80,100)
        if dagen == 31 and maanden >= 12:
          afgestoken += random.randrange(300,900)
        if dagen <= 1 and maanden == 1:
          afgestoken += random.randrange(1000,3000)
        if dagen >= 2 and maanden == 1:
          afgestoken = random.randrange(1,10)
        if dagen >= 7 and maanden == 1:
          afgestoken = random.randrange(1,3)
        if dagen >= 1 and maanden == 2:
          afgestoken = random.randrange(0,1)
        if dagen >= 1 and maanden == 1:
          graden = random.randrange(-10,12)
        if dagen >= 11 and maanden == 1:
          graden = random.randrange(-10,12)
        if dagen >= 21 and maanden == 1:
          graden = random.randrange(-10,12)
        if dagen >= 1 and maanden == 2:
          graden = random.randrange(-8,12)
        if dagen >= 11 and maanden == 2:
          graden = random.randrange(-8,12)
        if dagen >= 21 and maanden == 2:
          graden = random.randrange(-4,14)
        if dagen >= 1 and maanden == 3:
          graden = random.randrange(0,16)
        if dagen >= 11 and maanden == 3:
          graden = random.randrange(3,18)
        if dagen >= 21 and maanden == 3:
          graden = random.randrange(5,20)
        if dagen >= 1 and maanden == 4:
          graden = random.randrange(7,22)
        if dagen >= 11 and maanden == 4:
          graden = random.randrange(9,23)
        if dagen >= 21 and maanden == 4:
          graden = random.randrange(10,25)
        if dagen >= 1 and maanden == 5:
          graden = random.randrange(11,26)
        if dagen >= 11 and maanden == 5:
          graden = random.randrange(12,27)
        if dagen >= 21 and maanden == 5:
          graden = random.randrange(12,28)
        if dagen >= 1 and maanden == 6:
          graden = random.randrange(13,29)
        if dagen >= 11 and maanden == 6:
          graden = random.randrange(14,29)
        if dagen >= 21 and maanden == 6:
          graden = random.randrange(14,30)
        if dagen >= 1 and maanden == 7:
          graden = random.randrange(15,31)
        if dagen >= 11 and maanden == 7:
          graden = random.randrange(15,31)
        if dagen >= 21 and maanden == 7:
          graden = random.randrange(15,32)
        if dagen >= 1 and maanden == 8:
          graden = random.randrange(15,32)
        if dagen >= 11 and maanden == 8:
          graden = random.randrange(15,32)
        if dagen >= 21 and maanden == 8:
          graden = random.randrange(14,30)
        if dagen >= 1 and maanden == 9:
          graden = random.randrange(13,28)
        if dagen >= 11 and maanden == 9:
          graden = random.randrange(12,27)
        if dagen >= 21 and maanden == 3:
          graden = random.randrange(10,25)
        if dagen >= 1 and maanden == 10:
          graden = random.randrange(8,23)
        if dagen >= 11 and maanden == 10:
          graden = random.randrange(6,22)
        if dagen >= 21 and maanden == 10:
          graden = random.randrange(5,20)
        if dagen >= 1 and maanden == 11:
          graden = random.randrange(3,18)
        if dagen >= 11 and maanden == 11:
          graden = random.randrange(0,17)
        if dagen >= 21 and maanden == 11:
          graden = random.randrange(-2,15)
        if dagen >= 1 and maanden == 12:
          graden = random.randrange(-4,13)
        if dagen >= 11 and maanden == 12:
          graden = random.randrange(-6,12)
        if dagen >= 21 and maanden == 12:
          graden = random.randrange(-8,12)

      if event.key == pygame.K_d:
        dag(dagen)
        dagen -= 1
        dagnummer -= 1

      if event.key == pygame.K_q:
        pygame.quit = True


  screen.fill(wit)

# Verjaardag Florian
  if dagen == 6 and maanden == 6 and jaren >= 1996:
    verjaardagflorian = pygame.font.SysFont(None,70)
    verjaardagfloriantekst = verjaardagflorian.render(("gefeliciteerd florian"),True,zwart)
    screen.blit(verjaardagfloriantekst,[190,500])

  # Verjaardag Simon
  if dagen == 24 and maanden == 11 and jaren >= 1989:
    verjaardag = pygame.font.SysFont(None,70)
    verjaardagtekst = verjaardag.render(("Gefeliciteerd Simon"),True,zwart)
    screen.blit(verjaardagtekst,[190,500])

  # Dagnaam
  if dagnummer > 7:
    dagnummer = 1

  if dagnummer < 1:
    dagnummer = 7

  # Januari
  if dagen > 31 and maanden == 1:
    maanden = 2
    dagen = 1


  if dagen < 1 and maanden == 1:
    maanden = 12
    dagen = 31
    jaren -= 1

  # Februari met schrikkeljaar
  if dagen > 29 and maanden == 2 and schrikkeljaar(jaren) == 1:
    maanden = 3
    dagen = 1
    dagnummerloop = 1

  if dagen < 1 and maanden == 2:
    maanden = 1
    dagen = 1

  # Februari zonder schrikkeljaar
  if dagen > 28 and maanden == 2 and schrikkeljaar(jaren) == 0:
    maanden = 3
    dagen = 1

  # Maart
  if dagen > 31 and maanden == 3:
    maanden = 4
    dagen = 1


  if dagen < 1 and maanden == 3 and schrikkeljaar(jaren) == 0:
    maanden = 2
    dagen = 28

  if dagen < 1 and maanden == 3 and schrikkeljaar(jaren) == 1:
    maanden = 2
    dagen = 29

  # April
  if dagen > 30 and maanden == 4:
    maanden = 5
    dagen = 1

  if dagen < 1 and maanden == 4:
    maanden = 3
    dagen = 31

  # Mei
  if dagen > 31 and maanden == 5:
    maanden = 6
    dagen = 1

  if dagen < 1 and maanden == 5:
    maanden = 4
    dagen = 30

  # Juni
  if dagen > 30 and maanden == 6:
    maanden = 7
    dagen = 1

  if dagen < 1 and maanden == 6:
    maanden = 5
    dagen = 31

  # Juli
  if dagen > 31 and maanden == 7:
    maanden = 8
    dagen = 1

  if dagen < 1 and maanden == 7:
    maanden = 6
    dagen = 30

  # Augustus
  if dagen > 31 and maanden == 8:
    maanden = 9
    dagen = 1

  if dagen < 1 and maanden == 8:
    maanden = 7
    dagen = 31

  # September
  if dagen > 30 and maanden == 9:
    maanden = 10
    dagen = 1

  if dagen < 1 and maanden == 9:
    maanden = 8
    dagen = 31

  # Oktober
  if dagen > 31 and maanden == 10:
    maanden = 11
    dagen = 1

  if dagen < 1 and maanden == 10:
    maanden = 9
    dagen = 30

  # November
  if dagen > 30 and maanden == 11:
    maanden = 12
    dagen = 1

  if dagen < 1 and maanden == 11:
    maanden = 10
    dagen = 31

  # December
  if dagen > 31 and maanden == 12:
    maanden = 1
    dagen = 1
    jaren += 1

  if dagen < 1 and maanden == 12:
    maanden = 11
    dagen = 30

  if afgestoken < 0:
    afgestoken = 0

  uren += 1
  if uren > 100:
    dagen += 1
    dagnummer += 1
    maanlicht += (200/27.3)
    uren = 0
    temperatuur(graden)
    if dagen >= 1 and maanden == 1:
      graden = random.randrange(-10,12)
    if dagen >= 11 and maanden == 1:
      graden = random.randrange(-10,12)
    if dagen >= 21 and maanden == 1:
      graden = random.randrange(-10,12)
    if dagen >= 1 and maanden == 2:
      graden = random.randrange(-8,12)
    if dagen >= 11 and maanden == 2:
      graden = random.randrange(-8,12)
    if dagen >= 21 and maanden == 2:
      graden = random.randrange(-4,14)
    if dagen >= 1 and maanden == 3:
      graden = random.randrange(0,16)
    if dagen >= 11 and maanden == 3:
      graden = random.randrange(3,18)
    if dagen >= 21 and maanden == 3:
      graden = random.randrange(5,20)
    if dagen >= 1 and maanden == 4:
      graden = random.randrange(7,22)
    if dagen >= 11 and maanden == 4:
      graden = random.randrange(9,23)
    if dagen >= 21 and maanden == 4:
      graden = random.randrange(10,25)
    if dagen >= 1 and maanden == 5:
      graden = random.randrange(11,26)
    if dagen >= 11 and maanden == 5:
      graden = random.randrange(12,27)
    if dagen >= 21 and maanden == 5:
      graden = random.randrange(12,28)
    if dagen >= 1 and maanden == 6:
      graden = random.randrange(13,29)
    if dagen >= 11 and maanden == 6:
      graden = random.randrange(14,29)
    if dagen >= 21 and maanden == 6:
      graden = random.randrange(14,30)
    if dagen >= 1 and maanden == 7:
      graden = random.randrange(15,31)
    if dagen >= 11 and maanden == 7:
      graden = random.randrange(15,31)
    if dagen >= 21 and maanden == 7:
      graden = random.randrange(15,32)
    if dagen >= 1 and maanden == 8:
      graden = random.randrange(15,32)
    if dagen >= 11 and maanden == 8:
      graden = random.randrange(15,32)
    if dagen >= 21 and maanden == 8:
      graden = random.randrange(14,30)
    if dagen >= 1 and maanden == 9:
      graden = random.randrange(13,28)
    if dagen >= 11 and maanden == 9:
      graden = random.randrange(12,27)
    if dagen >= 21 and maanden == 3:
      graden = random.randrange(10,25)
    if dagen >= 1 and maanden == 10:
      graden = random.randrange(8,23)
    if dagen >= 11 and maanden == 10:
      graden = random.randrange(6,22)
    if dagen >= 21 and maanden == 10:
      graden = random.randrange(5,20)
    if dagen >= 1 and maanden == 11:
      graden = random.randrange(3,18)
    if dagen >= 11 and maanden == 11:
      graden = random.randrange(0,17)
    if dagen >= 21 and maanden == 11:
      graden = random.randrange(-2,15)
    if dagen >= 1 and maanden == 12:
      graden = random.randrange(-4,13)
    if dagen >= 11 and maanden == 12:
      graden = random.randrange(-6,12)
    if dagen >= 21 and maanden == 12:
      graden = random.randrange(-8,12)

    if maanlicht > 200:
      maanlicht = 0

  if minuten == 60:
    minuten = 0
    uur += 1
  
  if uur == 24:
    uur = 0 

  if dagen == 21 and maanden == 12:
    uur = 8
    minuten = 0
    uur2 = 17
    minuten2 = 0
  
  afsluittekst()
  jaar(jaren)
  maand(maanden)
  dag(dagen)
  tijd_uur()
  tijd_minuten()
  tijd_uur2()
  tijd_minuten2()
  pygame.display.update()
