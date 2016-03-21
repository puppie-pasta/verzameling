import random
print("hallo welkom getaller rader 2 voor beginnende amateur")
verzinner = random.randrange(1, 20)
rader = 0; aantal = 11
print("oke omdat dit het nivou beginnende amatuer is ga ik het een klein inniminni pietje moeilijker maken ik heb een getal van 1 tot 20")
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
        print("kunt u het echt niet beter ga opnieuw en verbeter je cijfers of speel een nivoutje makkelijker")
        
