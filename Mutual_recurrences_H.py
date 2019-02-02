m = pow(10, 9)


def xfunc(n):
    if n >= 0:
        return (xfunc(n-a)) % m + (yfunc(n-b)) % m + (yfunc(n-c)) % m + n*(pow(d, n))
    else:
        return 1

def yfunc(n):
    if n >= 0:
        return (yfunc(n-e)) % m + (xfunc(n-f)) % m + (xfunc(n-g)) % m + n*(pow(h, n))
    else:
        return 1

t = int(input())
for i in range(1, t+1):
    a, b, c, d, e, f, g, h, n = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    f = int(f)
    g = int(g)
    h = int(h)
    n = int(n)
    print(xfunc(n), yfunc(n))