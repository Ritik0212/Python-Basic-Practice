import random
print("roll dice")
play = True
while play:
    a = random.randrange(1,7,1)
    print(a)
    if input('wanna roll again? y or n')=='n':
        play = False