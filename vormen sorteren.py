import pygame
import random

pygame.init()

wit = (255,255,255)
zwart = (0,0,0)
geel = (255,255,0)
groen = (0,255,0)
rood = (255,0,0)
zwart = (0,0,0)

screen = pygame.display.set_mode((1000,1000))
screen.fill(wit)

vormen = random.randrange(1,4)
bakken = 0

def tekst():
  font = pygame.font.SysFont(None,30)
  text = font.render("zet de vormpjes in de juiste doos",True,zwart)
  screen.blit(text,[500,50])


def fout():
  font = pygame.font.SysFont(None,100)
  text = font.render("fout",True,rood)
  screen.blit(text,[500,500])

def goed():
  font = pygame.font.SysFont(None,100)
  text = font.render("goed",True,groen)
  screen.blit(text,[500,500])

def rechthoekbak():
  pygame.draw.rect(screen,geel,[100,100,200,300])
  font = pygame.font.SysFont(None,30)
  text = font.render("rechthoek",True,zwart)
  screen.blit(text,[100,100])

def circelbak():
  pygame.draw.rect(screen,geel,[400,100,200,300])
  font = pygame.font.SysFont(None,30)
  text = font.render("circel",True,zwart)
  screen.blit(text,[400,100])

def vierhoekbak():
  pygame.draw.rect(screen,geel,[700,100,200,300])
  font = pygame.font.SysFont(None,30)
  text = font.render("vierhoek",True,zwart)
  screen.blit(text,[700,100])

def rechthoek():
  pygame.draw.rect(screen,zwart,[500,500,200,100])

def circel():
  pygame.draw.circle(screen,zwart,[500,500],100)

def vierhoek():
  pygame.draw.rect(screen,zwart,[500,500,100,100])

exit = False

while not exit:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q:
        exit = True
      if event.key == pygame.K_r:
        vormen = random.randrange(1,4)
        bakken = 0  

  muis = pygame.mouse.get_pos()
  klik = pygame.mouse.get_pressed()
  
  if klik[0]:
    if 100+200 > muis[0] > 100 and 100+200 > muis[1] > 100:
      bakken = 3
  
  if klik[0]:
    if 400+200 > muis[0] > 400 and 400+200 > muis[1] > 100:
      bakken = 2

  if klik[0]:
    if 700+200 > muis[0] > 700 and 700+200 > muis[1] > 100:
      bakken = 1             
  
  screen.fill(wit)

  if vormen == 1:
  	vierhoek()
  if vormen == 2:
    circel()
  if vormen == 3:
    rechthoek()  

  if vormen == bakken:
    goed()
  if vormen != bakken and bakken > 0:
    fout()    

  if bakken == 0:
    tekst()        	

  rechthoekbak()
  circelbak()
  vierhoekbak()
  pygame.display.update()
