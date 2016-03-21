import random
print("hallo welkom getaller rader voor legeredarich")
verzinner = random.randrange(1, 1000000)
rader = 0; aantal = 11
print("waarschuwing dit nivou is apsoluut niet geschikt voor beginners hier is het hoogste nivou ik heb een getal van 1 tot de 1000000 in gedachten")
while 1:
    rader = int(input("raad het maar"))
    aantal = aantal - 1
    if rader == verzinner:
        print("goed geraden")
        break
    else:
        if rader < verzinner:
            print("nee hoger")
        else:
            print("nee lager")
print("ik vondt het leuk om met je te spelen je krijgt van mij un",aantal,"als cijfer")
