import random
print("hallo welkom bij getalen rader voor beginnende amateur")
verzinner = random.randrange(1, 20)
rader = 0; aantal = 11
print("oke omdat dit het beginnende amateur is ga ik het een klein innemini moeilijker maken ik heb een getal van 1 tot de 20")
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
