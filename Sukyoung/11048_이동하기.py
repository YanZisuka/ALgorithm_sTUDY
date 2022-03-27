N, M = map(int,input().split())
candy = [[0]*(M+1)] + [[0]+list(map(int,input().split())) for _  in range(N)]

for row in range(1,N+1):
    for col in range(1,M+1):
        candy[row][col] += max(candy[row-1][col],candy[row][col-1]) # 자기 위 vs 왼쪽 비교

print(candy[N][M])
