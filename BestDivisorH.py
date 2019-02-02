import math

def show_divisors(n):
    kist=[]
    j=0
    for i in range(1,int(math.sqrt(n))+2):
        if n%i==0:
            if n/i==i:
                kist.insert(j,i)
                j+=1
            else:
                kist.insert(j,i)
                j+=1
                kist.insert(j,int(n/i))
                j+=1
    return kist



def sum_of_digits(k):
    sum = 0

    while(k != 0):
        sum += k%10
        k = math.floor(k/10)
    return sum
b=81
x = show_divisors(b)
m = sum_of_digits(x[0])
ans = x[0]
for k in range(1,len(x)):
    if m < sum_of_digits(x[k]):
        m = sum_of_digits(x[k])
        ans = x[k]
    elif m == sum_of_digits(x[k]):
        if ans > x[k]:
            ans = x[k]
print(ans)