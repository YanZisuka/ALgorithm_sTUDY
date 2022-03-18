n, k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
coin = sorted(coin,reverse=True)
print(coin)
i = 0
result1 = 0
while k>0:
    result1 += k//coin[i]
    k = k%coin[i]
    i+=1
print(result1)

i = 1
result2 = 0
while k>0:
    result2 += k//coin[i]
    k = k%coin[i]
    i+=1
print(result2)