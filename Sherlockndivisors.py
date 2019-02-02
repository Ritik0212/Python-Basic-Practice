import math

def show_divisors(n):
    kist=[]
    j=0
    for i in range(1,int(math.sqrt(n))+1):
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

x=show_divisors(12)
print(x)
count=0
for i in range(0,len(x)):
    if x[i]%2==0:
        count+=1
print(count)


