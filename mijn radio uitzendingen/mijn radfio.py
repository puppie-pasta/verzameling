import pygame

pygame.init()

wit = (255,255,255)

screen = pygame.display.set_mode((800,600))
screen.fill(wit)

tijd = 0

exit = False

while not exit:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q:
        exit = True

  klok = pygame.time.Clock()

  muziek2 = pygame.mixer.Sound("Feyenoord_Lied.wav")
  muziek1 = pygame.mixer.Sound("Feyenoord_-_Hand_in_Hand_Kameraden.wav")
  nieuws = pygame.mixer.Sound("het nieuws op 17-1-2016(1).wav")
  if tijd == 1:
    pygame.mixer.Sound.play(nieuws)
  if tijd == 451:
  	pygame.mixer.Sound.play(muziek1)
  if tijd == 676:
    pygame.mixer.Sound.play(muziek2)    	

  tijd += 1
  klok.tick(1)
  pygame.display.update()