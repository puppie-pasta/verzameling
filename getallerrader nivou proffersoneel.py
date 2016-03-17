import random
print("hallo welkom bij getaller rader voor proffersoneel")
verzinner = random.randrange(1, 10000)
rader = 0; aantal = 11
print("oke dit is een vrij hoog nivou van getallerrader proffersoneel ik heb een getal van 1 tot de 10000 in gedachten")
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
