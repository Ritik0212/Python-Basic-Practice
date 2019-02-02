import math

N = int(input())
xs = []
ys = []

for i in range(1, N+1):
    x, y = (input().split())
    x = int(x)
    y = int(y)
    xs.append(x)
    ys.append(y)

xn = min(xs)
xp = max(xs)
yn = min(ys)
yp = max(ys)
value1 = xp-xn
value2 = yp-yn
value3 = math.sqrt((yp*yp)+(xn*xn))
value4 = math.sqrt((yn*yn)+(xn*xn))
value5 = math.sqrt((yp*yp)+(xp*xp))
value6 = math.sqrt((yp*yp)+(xp*xp))
ans = max(value1, value2, value3, value4, value5, value6)
print('{0:.6f}'.format(ans))