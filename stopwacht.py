import pygame

pygame.init()

zwart = (0,0,0)
wit = (255,255,255)

screen = pygame.display.set_mode((1000,1000))
screen.fill(zwart)

tijd = 0
seconde = 0
minuten = 0
uur = 0

def pauze_tekst():
  font = pygame.font.SysFont(None,30)
  text = font.render("druk op de p voor pauze druk op start om veder te gaan druk op r om te resseten",True,wit)
  screen.blit(text,[0,200])

def aantal_uur(uur):
  font = pygame.font.SysFont(None,50)
  text = font.render(str(uur),True,wit)
  screen.blit(text,[800,100])

def aantal_minuten(minuten):
  font = pygame.font.SysFont(None,50)
  text = font.render(":"+str(minuten),True,wit)
  screen.blit(text,[850,100])

def aantal_seconde(seconde):
  font = pygame.font.SysFont(None,50)
  text = font.render(":"+str(seconde),True,wit)
  screen.blit(text,[900,100])

exit = False

while not exit:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q:
        exit = True
      if event.key == pygame.K_p:
        tijd = -3000
      if event.key == pygame.K_s:
        tijd = 0
      if event.key == pygame.K_r:
        seconde = 0
        minuten = 0
        uur = 0    

  tijd += 1

  if tijd == 500:
    tijd = 0
    seconde += 1

  if seconde == 60:
    seconde = 0
    minuten += 1

  if minuten == 60:
    minuten = 0
    uur += 1            
  
  screen.fill(zwart)
  aantal_seconde(seconde)
  aantal_minuten(minuten)
  aantal_uur(uur)
  pauze_tekst()
  pygame.display.update()