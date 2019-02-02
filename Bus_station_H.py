N = int(input())
numbers = [int(x) for x in input().split()]
ans = []
mnsr = max(numbers)
mxsr = sum(numbers)

for i in range(mnsr, mxsr+1):
    sum1 = i
    j = 0
    while sum1 == i and j <= N-1:
        sum1 = 0
        while sum1 < i and j <= N-1:
            sum1 = sum1 + numbers[j]
            j = j + 1
    if j == N and sum1 == i:
        ans.append(i)
print(*ans)