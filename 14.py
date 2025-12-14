import random
r = int(input("Digite um numero"))
r = random.randint(1,20)
acertou = False
while (not acertou):
    chance = int(input("digite seu numero"))
    if (chance != r):
        print("errou")
    else:
        print("acertou")
        acertou = True