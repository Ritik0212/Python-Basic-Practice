def fact(n):
    if n > 0:
        return n*fact(n-1)
    elif n == 0:
        return 1

n = int(input('Enter a non negative integer'))
if n < 0:
    print("It is not a non negative integer, please run again")
else:
    print('factorial of this number is:', fact(n))
