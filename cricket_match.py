import random
w1 = 0
w2 = 0
score1 = 0
score2 = 0
abc = ''
while (w1 != 5 and w2 != 5) and abc != 'q':
    abc = str(input('Hit a shot by pressing s or press q to quit'))
    if abc == 's':
        x = random.randrange(0, 7, 1)
        if x == 0:
            w1 += 1
            print('wicket fall')
            print('your score is:', score1, '/', w1)
        else:
            score1 += x
            print('You hit', x)
            print('your score is:', score1, '/', w1)

        print('Its computers turn now')
        y = random.randrange(0, 7, 1)
        if y == 0:
            w2 += 1
            print('wicket fall')
            print('computer score is:', score2, '/', w2)
        else:
            score2 += y
            print('computer hit', y)
            print('computer score is:', score2, '/', w2)
        if w1 == 5 or w2 == 5:
            if score1 >= score2:
                print('You won')
            else:
                print('You loss')