n, k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
coin.sort()
for i in coin:
    k//i