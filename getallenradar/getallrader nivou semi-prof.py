import random
print("hallo welkom bij getaller rader voor semi-prof")
verzinner = random.randrange(1, 1000)
rader = 0; aantal = 11
print("oke dit is getallerader voor semi-prof nivou ik heb een getal van 1 tot de 1000 in gedachten")
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
