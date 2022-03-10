N = int(input())
train = [0]+list(map(int,input().split()))
M = int(input())

for i in range(N):
    train[i+1]+=train[i]  # 누적합 리스트 만들기 (이 코드 추가하면 python3 통과 - 구간합 계산이 빠름)

dp = [[0]*(N+1) for _ in range(4)]  # dp 2차원 리스트 만들기
for i in range(1,4):
    for j in range(i*M,1+N):
        dp[i][j] = max(dp[i][j-1],train[j]-train[j-M]+dp[i-1][j-M])  # max(바로 앞의 값 , 구간합+전 행의 누적합)

print(dp[3][N])