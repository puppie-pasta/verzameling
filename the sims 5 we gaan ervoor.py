import pygame

pygame.init()

groen = (0,255,0)
oranje = (255,200,0)
grijs = (200,200,200)
blauw = (0,0,255)
lichtblauw = (100,100,255)
wit = (255,255,255)
klikblauw = (120,120,255)
bruin = (100,0,0)
zwart = (0,0,0)
klikzwart = (10,10,10)
rood = (255,0,0)

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("The Sims 5")
screen.fill(groen)

x1 = 400
y1 = 300
x2 = 590
y2 = 590
x3 = 590
y3 = 550
x4 = 390
y4 = 590
x5 = 390
y5 = 550
x6 = 190
y6 = 590
x2_speed = float(-0.1)
y2_speed = 0
x3_speed = float(-0.005)
y3_speed = 0
x4_speed = float(-0.001)
y4_speed = 0
x5_speed = float(-0.003)
y5_speed = 0
x6_speed = float(-0.03)
y6_speed = 0
simleeftijddagen = 0

def grafsteen():
  pygame.draw.rect(screen,grijs,[700,300,50,80])

def simjaartal(simleeftijddagen):
  font = pygame.font.SysFont(None,30)
  text = font.render("leeftijd"+str(simleeftijddagen),True,zwart)
  screen.blit(text,[100,40])


def dood():
  font = pygame.font.SysFont(None,50)
  text = font.render("overleden: je sim is helaas overleden",True,rood)
  screen.blit(text,[0,400])

def babysim(x1,y1):
  pygame.draw.circle(screen,oranje,[x1,y1],3)

def peutersim(x1,y1):
  pygame.draw.circle(screen,oranje,[x1,y1],5)

def kindersim(x1,y1):
  pygame.draw.circle(screen,oranje,[x1,y1],10)

def pubersim(x1,y1):
  pygame.draw.circle(screen,oranje,[x1,y1],17) 


def bejaardsim(x1,y1):
  pygame.draw.circle(screen,grijs,[x1,y1],17)

def sim(x1,y1):
	pygame.draw.circle(screen,oranje,[x1,y1],20)

def simleeftijd(simleeftijddagen):
  pygame.draw.rect(screen,rood,[10,10,100,30])
  pygame.draw.rect(screen,wit,[10,10,simleeftijddagen,30])  

klok = pygame.time.Clock()

exit = False

while not exit:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q:
        exit = True

  muis = pygame.mouse.get_pos()
  klik = pygame.mouse.get_pressed()

  if klik[0]:
    if 305+20 > muis[0] > 305 and 105+20 > muis[1] > 105:
      x1 = 305
      y1 = 105
      x3_speed = float(0.015)
  if klik[2]:
    screen.fill(groen)
    x1 = 400
    y1 = 300
    x3_speed = float(-0.005)      

  if klik[0]:
  	if 500+80 > muis[0] > 500 and 300+30 > muis[1] > 300:
  	  pygame.draw.rect(screen,grijs,[muis[0]+100,muis[1]+100,80,30])
  if klik[0]:
    if 500+80 > muis[0] > 500 and 300+30 > muis[1] > 300:
      x1 = 500
      y1 = 300 
      x2_speed = float(0.03)
  if klik[2]:
  	screen.fill(groen)
  	x1 = 400
  	y1 = 300
  	x2_speed = float(-0.01)

  if klik[0]:
    if 500+35 > muis[0] > 500 and 100+55 > muis[1] > 100:
      x4_speed = float(0.003)
      x1 = 500
      y1 = 100
  if klik[2]:
    x1 = 400
    y1 = 300
    x4_speed = float(-0.001)  	
  
  if x2 < 500:
    dood()
    grafsteen()
    x2_speed = 0
    simleeftijddagen += 0
    simleeftijddagen = 100

  if x3 < 500:
    font = pygame.font.SysFont(None,20)
    text = font.render("je sim is in slaap gevallen",True,rood)
    screen.blit(text,[400,300])
    x3_speed = float(0.015)
  if x3 == 520:
    x3_speed = float(-0.005)

  if klik[0]:
    if 300+50 > muis[0] > 300 and 200+15 > muis[1] > 200:
      x5_speed = float(0.009)
      x1 = 300
      y1 = 200
  if klik[2]:
    x5_speed = float(-0.003)
    x1 = 400
    y1 = 300

  if klik[0]:
    if 580+15 > muis[0] > 580 and 130+15 > muis[1] > 130:
      x6_speed = float(0.09)
      x1 = 580
      y1 = 130
  if klik[2]:
    x6_speed = float(-0.03)
    x1 = 400
    y1 = 300

  if x6 < 100:
    x6_speed = float(0.09)
    font = pygame.font.SysFont(None,20)
    text = font.render("je sim heeft in zijn broek geplast",True,rood)
    screen.blit(text,[400,300])

  if x6 == 190:
    x6_speed = float(-0.03)              	
          	
  screen.fill(groen)
  pygame.draw.rect(screen,bruin,[300,100,300,300])
  pygame.draw.rect(screen,zwart,[500,300,80,30])    
  pygame.draw.circle(screen,blauw,[0,500],100)
  pygame.draw.rect(screen,blauw,[0,500,800,100])
  pygame.draw.rect(screen,zwart,[500,580,100,20])
  pygame.draw.rect(screen,wit,[x2,y2,10,10])
  font = pygame.font.SysFont(None,20)
  text = font.render("eten",True,zwart)
  screen.blit(text,[500,560])
  pygame.draw.rect(screen,wit,[300,100,100,30])
  pygame.draw.rect(screen,zwart,[300,100,30,30])
  pygame.draw.rect(screen,wit,[305,105,20,20])
  pygame.draw.rect(screen,zwart,[500,540,100,20])
  pygame.draw.rect(screen,wit,[x3,y3,10,10])
  font = pygame.font.SysFont(None,20)
  text = font.render("slapen",True,zwart)
  screen.blit(text,[500,520])
  pygame.draw.rect(screen,wit,[500,100,40,60])
  pygame.draw.rect(screen,blauw,[500,100,35,55])
  pygame.draw.rect(screen,zwart,[300,580,100,20])
  pygame.draw.rect(screen,wit,[x4,y4,10,10])
  font = pygame.font.SysFont(None,20)
  text = font.render("douchen",True,zwart)
  screen.blit(text,[300,560])
  pygame.draw.rect(screen,rood,[300,200,50,15])
  pygame.draw.rect(screen,zwart,[350,200,20,3])
  pygame.draw.rect(screen,zwart,[300,540,100,20])
  pygame.draw.rect(screen,wit,[x5,y5,10,10])
  font = pygame.font.SysFont(None,20)
  text = font.render("sociaal",True,zwart)
  screen.blit(text,[300,520])
  pygame.draw.rect(screen,zwart,[100,580,100,20])
  pygame.draw.rect(screen,wit,[x6,y6,10,10])
  pygame.draw.circle(screen,wit,[580,130],20)
  pygame.draw.circle(screen,blauw,[580,130],15)
  font = pygame.font.SysFont(None,20)
  text = font.render("wc",True,zwart)
  screen.blit(text,[100,560])

  if simleeftijddagen >= 0 and simleeftijddagen < 2:
    babysim(x1,y1)
  if simleeftijddagen >= 2 and simleeftijddagen < 4:
    peutersim(x1,y1)
  if simleeftijddagen >= 4 and simleeftijddagen < 12:
    kindersim(x1,y1)
  if simleeftijddagen >= 12 and simleeftijddagen < 18:
    pubersim(x1,y1)
  if simleeftijddagen >= 18 and simleeftijddagen < 65:
    sim(x1,y1)
  if simleeftijddagen >= 65 and simleeftijddagen < 100:
    bejaardsim(x1,y1)
  if simleeftijddagen >= 100:
    dood()
    grafsteen()
    simleeftijddagen = 100
    x2_speed = 0
    x3_speed = 0
    x4_speed = 0
    x5_speed = 0
    x6_speed = 0             

  x2 += x2_speed
  y2 += y2_speed
  x3 += x3_speed
  y3 += y3_speed
  x4 += x4_speed
  y4 += y4_speed
  x5 += x5_speed
  y5 += y5_speed
  x6 += x6_speed
  y6 += y6_speed
  klok.tick(60)
  simleeftijd(simleeftijddagen)
  simjaartal(simleeftijddagen)
  simleeftijddagen += float(0.1)
  pygame.display.update()
