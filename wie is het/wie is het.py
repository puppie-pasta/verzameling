import pygame

pygame.init()

wit = (255,255,255)
zwart = (0,0,0)
grijs = (200,200,200)

screen = pygame.display.set_mode((1000,1000))
screen.fill(wit)

x_foto_anne = 0
y_foto_anne = 0

x_foto_bert = 100
y_foto_bert = 0

x_foto_koos = 200
y_foto_koos = 0

x_foto_lotte = 300
y_foto_lotte = 0

x_foto_jacco = 500
y_foto_jacco = 200

x_foto_kees = 400
y_foto_kees = 0

x_foto_piet = 500
y_foto_piet = 0

x_foto_hans = 600
y_foto_hans = 0

x_foto_chris = 700
y_foto_chris = 0

x_foto_eliza = 800
y_foto_eliza = 0

x_foto_thoe = 900
y_foto_thoe = 0

x_foto_geert = 0
y_foto_geert = 200

x_foto_rob = 100
y_foto_rob = 200

x_foto_henk = 200
y_foto_henk = 200

x_foto_gerrit = 300
y_foto_gerrit = 200

x_foto_jaap = 400
y_foto_jaap = 200

x_foto_truus = 600
y_foto_truus = 200

x_foto_teun = 700
y_foto_teun = 200

x_foto_frans = 800
y_foto_frans = 200

x_foto_els = 900
y_foto_els = 200

x_foto_fret = 0
y_foto_fret = 400

x_foto_bram = 100
y_foto_bram = 400

x_foto_bart = 200
y_foto_bart = 400

x_foto_ronalt = 300
y_foto_ronalt = 400

def vraag8_knop():
  pygame.draw.rect(screen,grijs,[200,600,90,30])
  font = pygame.font.SysFont(None,10)
  text = font.render("heeft hij/zij donkere ogen?",True,zwart)
  screen.blit(text,[600,600])

def vraag7_knop():
  pygame.draw.rect(screen,grijs,[200,600,90,30])
  font = pygame.font.SysFont(None,10)
  text = font.render("heeft hij/zij lichte ogen?",True,zwart)
  screen.blit(text,[500,600])

def vraag6_knop():
  pygame.draw.rect(screen,grijs,[200,600,90,30])
  font = pygame.font.SysFont(None,10)
  text = font.render("heeft hij/zij donker haar?",True,zwart)
  screen.blit(text,[600,600])

def vraag5_knop():
  pygame.draw.rect(screen,grijs,[200,600,90,30])
  font = pygame.font.SysFont(None,10)
  text = font.render("heeft hij/zij licht haar?",True,zwart)
  screen.blit(text,[500,600])

def vraag4_knop():
  pygame.draw.rect(screen,grijs,[200,600,90,30])
  font = pygame.font.SysFont(None,10)
  text = font.render("heeft hij een snor?",True,zwart)
  screen.blit(text,[400,600])

def vraag4_knop():
  pygame.draw.rect(screen,grijs,[200,600,90,30])
  font = pygame.font.SysFont(None,10)
  text = font.render("heeft hij een baart?",True,zwart)
  screen.blit(text,[300,600])

def vraag3_knop():
  pygame.draw.rect(screen,grijs,[200,600,90,30])
  font = pygame.font.SysFont(None,30)
  text = font.render("draagt hij/zij een bril?",True,zwart)
  screen.blit(text,[200,600])

def vraag2_knop():
  pygame.draw.rect(screen,grijs,[100,600,90,30])
  font = pygame.font.SysFont(None,10)
  text = font.render("heeft het een ped op?",True,zwart)
  screen.blit(text,[100,600])

def vraag1_knop():
  pygame.draw.rect(screen,grijs,[0,600,100,40])
  font = pygame.font.SysFont(None,10)
  text = font.render("is het een man?",True,zwart)
  screen.blit(text,[0,600])

def truus():
  foto_truus = pygame.image.load("truus.png").convert()
  screen.blit(foto_truus,[x_foto_truus,y_foto_truus])
  font = pygame.font.SysFont(None,30)
  text = font.render("truus",True,zwart)
  screen.blit(text,[x_foto_truus,y_foto_truus])

def teun():
  foto_teun = pygame.image.load("teun.png").convert()
  screen.blit(foto_teun,[x_foto_teun,y_foto_teun])
  font = pygame.font.SysFont(None,30)
  text = font.render("teun",True,zwart)
  screen.blit(text,[x_foto_teun,y_foto_teun])

def frans():
  foto_frans = pygame.image.load("frans.png").convert()
  screen.blit(foto_frans,[x_foto_frans,y_foto_frans])
  font = pygame.font.SysFont(None,30)
  text = font.render("frans",True,zwart)
  screen.blit(text,[x_foto_frans,y_foto_frans])

def els():
  foto_els = pygame.image.load("els.png").convert()
  screen.blit(foto_els,[x_foto_els,y_foto_els])
  font = pygame.font.SysFont(None,30)
  text = font.render("els",True,zwart)
  screen.blit(text,[x_foto_els,y_foto_els])

def fret():
  foto_fret = pygame.image.load("fret.png").convert()
  screen.blit(foto_fret,[x_foto_fret,y_foto_fret])
  font = pygame.font.SysFont(None,30)
  text = font.render("fret",True,zwart)
  screen.blit(text,[x_foto_fret,y_foto_fret])

def bram():
  foto_bram = pygame.image.load("bram.png").convert()
  screen.blit(foto_bram,[x_foto_bram,y_foto_bram])
  font = pygame.font.SysFont(None,30)
  text = font.render("bram",True,zwart)
  screen.blit(text,[x_foto_bram,y_foto_bram])

def bart():
  foto_bart = pygame.image.load("bart.png").convert()
  screen.blit(foto_bart,[x_foto_bart,y_foto_bart])
  font = pygame.font.SysFont(None,30)
  text = font.render("bart",True,zwart)
  screen.blit(text,[x_foto_bart,y_foto_bart])

def ronalt():
  foto_ronalt = pygame.image.load("ronalt.png").convert()
  screen.blit(foto_ronalt,[x_foto_ronalt,y_foto_ronalt])
  font = pygame.font.SysFont(None,30)
  text = font.render("ronalt",True,zwart)
  screen.blit(text,[x_foto_ronalt,y_foto_ronalt])

def chris():
  foto_chris = pygame.image.load("chris.png").convert()
  screen.blit(foto_chris,[x_foto_chris,y_foto_chris])
  font = pygame.font.SysFont(None,30)
  text = font.render("chris",True,zwart)
  screen.blit(text,[x_foto_chris,y_foto_chris])

def eliza():
  foto_eliza = pygame.image.load("eliza.png").convert()
  screen.blit(foto_eliza,[x_foto_eliza,y_foto_eliza])
  font = pygame.font.SysFont(None,30)
  text = font.render("eliza",True,zwart)
  screen.blit(text,[x_foto_eliza,y_foto_eliza])

def thoe():
  foto_thoe = pygame.image.load("thoe.png").convert()
  screen.blit(foto_thoe,[x_foto_thoe,y_foto_thoe])
  font = pygame.font.SysFont(None,30)
  text = font.render("thoe",True,zwart)
  screen.blit(text,[x_foto_thoe,y_foto_thoe])

def geert():
  foto_geert = pygame.image.load("geert.png").convert()
  screen.blit(foto_geert,[x_foto_geert,y_foto_geert])
  font = pygame.font.SysFont(None,30)
  text = font.render("geert",True,zwart)
  screen.blit(text,[x_foto_geert,y_foto_geert])

def rob():
  foto_rob = pygame.image.load("rob.png").convert()
  screen.blit(foto_rob,[x_foto_rob,y_foto_rob])
  font = pygame.font.SysFont(None,30)
  text = font.render("rob",True,zwart)
  screen.blit(text,[x_foto_rob,y_foto_rob])

def henk():
  foto_henk = pygame.image.load("henk.png").convert()
  screen.blit(foto_henk,[x_foto_henk,y_foto_henk])
  font = pygame.font.SysFont(None,30)
  text = font.render("henk",True,zwart)
  screen.blit(text,[x_foto_henk,y_foto_henk])

def gerrit():
  foto_gerrit = pygame.image.load("gerrit.png").convert()
  screen.blit(foto_gerrit,[x_foto_gerrit,y_foto_gerrit])
  font = pygame.font.SysFont(None,30)
  text = font.render("gerrit",True,zwart)
  screen.blit(text,[x_foto_gerrit,y_foto_gerrit])

def jaap():
  foto_jaap = pygame.image.load("jaap.png").convert()
  screen.blit(foto_jaap,[x_foto_jaap,y_foto_jaap])
  font = pygame.font.SysFont(None,30)
  text = font.render("jaap",True,zwart)
  screen.blit(text,[x_foto_jaap,y_foto_jaap])

def jacco():
  foto_jacco = pygame.image.load("jacco.png").convert()
  screen.blit(foto_jacco,[x_foto_jacco,y_foto_jacco])
  font = pygame.font.SysFont(None,30)
  text = font.render("jacco",True,zwart)
  screen.blit(text,[x_foto_jacco,y_foto_jacco])

def kees():
  foto_kees = pygame.image.load("kees.png").convert()
  screen.blit(foto_kees,[x_foto_kees,y_foto_kees])
  font = pygame.font.SysFont(None,30)
  text = font.render("kees",True,zwart)
  screen.blit(text,[x_foto_kees,y_foto_kees])

def piet():
  foto_piet = pygame.image.load("piet.png").convert()
  screen.blit(foto_piet,[x_foto_piet,y_foto_piet])
  font = pygame.font.SysFont(None,30)
  text = font.render("piet",True,zwart)
  screen.blit(text,[x_foto_piet,y_foto_piet])

def hans():
  foto_hans = pygame.image.load("hans.png").convert()
  screen.blit(foto_hans,[x_foto_hans,y_foto_hans])
  font = pygame.font.SysFont(None,30)
  text = font.render("hans",True,zwart)
  screen.blit(text,[x_foto_hans,y_foto_hans])

def koos():
  foto_koos = pygame.image.load("koos.png").convert()
  screen.blit(foto_koos,[x_foto_koos,y_foto_koos])
  font = pygame.font.SysFont(None,30)
  text = font.render("koos",True,zwart)
  screen.blit(text,[x_foto_koos,y_foto_koos])

def lotte():
  foto_lotte = pygame.image.load("lotte.png").convert()
  screen.blit(foto_lotte,[x_foto_lotte,y_foto_lotte])
  font = pygame.font.SysFont(None,30)
  text = font.render("lotte",True,zwart)
  screen.blit(text,[x_foto_lotte,y_foto_lotte])

def bert():
  foto_bert = pygame.image.load("bert.png").convert()
  screen.blit(foto_bert,[x_foto_bert,y_foto_bert])
  font = pygame.font.SysFont(None,30)
  text = font.render("bert",True,zwart)
  screen.blit(text,[x_foto_bert,y_foto_bert])

def anne():
  foto_anne = pygame.image.load("anne.png").convert()
  screen.blit(foto_anne,[x_foto_anne,y_foto_anne])
  font = pygame.font.SysFont(None,30)
  text = font.render("anne",True,zwart)
  screen.blit(text,[x_foto_anne,y_foto_anne]) 

exit = False

while not exit:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q:
        exit = True

  screen.fill(wit)
  anne()
  bert()
  koos()
  lotte()
  hans()
  piet()
  kees()
  jacco()
  chris()
  thoe()
  eliza()
  geert()
  rob()
  henk()
  gerrit()
  jaap()
  truus()
  teun()
  frans()
  els()
  fret()
  bram()
  bart()
  ronalt()
  pygame.display.update()