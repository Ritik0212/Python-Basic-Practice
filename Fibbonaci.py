def fibbo(n):
    if n > 2:
        return fibbo(n-1) + fibbo(n-2)
    elif n == 1:
        return 0
    elif n == 2:
        return 1

nterms = int(input('Enter a positive integer'))
if nterms <= 0:
    print("It is not a positive integer, please run again")
else:
    print("Fibonacci sequence:")
    for i in range(1, nterms+1):
        print(fibbo(i))
