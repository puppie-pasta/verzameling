import random
print("hallo welkom bij getallerrader 2 voor een vrij hoog nivou proffersoneel")
verzinner = random.randrange(1, 10000)
rader = 0; aantal = 11
print("oke laten we beginnen ik heb een getal van 1 tot de 10000")
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
    print("zeer goed gespeeld")
else:
    if aantal < 6:
        print("kunt u het echt niet beter verbeter je cijfers blijft je cijfers onder de 6 speel een nivoutje lager")
        
