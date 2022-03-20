n, k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
coin.sort()
count = [0]*(k+1)

for i in range(1,k+1):
    count[i] = -1
    if i>=coin[0]:
        count[i] = count[i-coin[0]]+1

    for j in range(1,n):
        if i>=coin[j]:
            if count[i]*(count[i - coin[j]] + 1) != 0:
                count[i] = min(count[i],count[i - coin[j]] + 1)
            elif count[i] == 0:
                count[i] = count[i - coin[j]] + 1

    if count[i] == 0:
        count[i] = -1

print(count[k])
