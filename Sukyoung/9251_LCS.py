str1 = input()
str2 = input()
dp = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]
for i in range(1,len(str2)+1):  # 단어1 - 행
    for j in range(1,len(str1)+1):  # 단어2 - 열
        if str1[j-1]==str2[i-1]:  # 같은 스펠링이면
            dp[i][j] = dp[i-1][j-1]+1  # 대각선 방향 +1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])  # 위와 왼쪽중 큰 수
print(dp[len(str2)][len(str1)])
