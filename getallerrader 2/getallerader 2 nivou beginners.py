import random
print("hallo welkom getaller rader 2 nieuw is dat je nu commetaar krijgt op je cijfers oke dit is getaller rader 2 voor beginners")
verzinner = random.randrange(1, 10)
rader = 0; aantal = 11
print("oke omdat dit het beginner nivou is ga ik het niet te moeilijk maken ik heb een getal van tot 1 tot de 10 in gedachten")
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
if aantal >= 6:
    print("zeer goed gedaan")
else:
    if aantal <  6:
        print("kunt u het echt niet beter speel opnieuw en verbeter je cijfers")
        
