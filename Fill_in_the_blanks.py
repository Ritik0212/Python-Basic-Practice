import random

ans = 'correct'
score = 0
while ans != 'wrong':
    x = random.randrange(0, 10, 1)
    y = random.randrange(0, 10, 1)
    z = random.randrange(0, 4, 1)
    if z == 0:
        if int(input(str(x) + '+' + str(y) + '=?')) == x + y:
            ans = 'correct'
        else:
            ans = 'wrong'
    if z == 1:
        if int(input(str(x) + '-' + str(y) + '=?')) == x - y:
            ans = 'correct'
        else:
            ans = 'wrong'
    if z == 2:
        if int(input(str(x) + '*' + str(y) + '=?')) == x * y:
            ans = 'correct'
        else:
            ans = 'wrong'
    if z == 3:
        if y != 0:
            if int(input(str(x) + '/' + str(y) + '=?')) == int(x / y):
                ans = 'correct'
            else:
                ans = 'wrong'
        else:
            ZeroDivisionError('division by zero')
    score += 1
if ans == 'wrong':
    print('bro u r wrong this time, your final score:', score)
