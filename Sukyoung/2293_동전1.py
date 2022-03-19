n, k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
coin.sort()
count = [0]*(k+1)
count[0] = 1
for c in coin:  # 동전 가치
    for i in range(1,k+1): # 가치의 합
        if i >= c:
            count[i]+=count[i-c] # 동전이 2면, 자신보다 -2 적은 가치의 경우에 다 +2를 해주면 되기 때문

print(count[k])

