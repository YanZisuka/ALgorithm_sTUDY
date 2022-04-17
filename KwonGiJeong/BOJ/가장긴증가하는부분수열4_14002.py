N = int(input())
data = list(map(int, input().split()))
dp = [1] * (N + 1)

for i in range(N):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j] + 1)

max_len = max(dp)
print(max_len)

answer = []
for i in range(N - 1, -1, -1):
    if dp[i] == max_len:
        answer.append(data[i])
        max_len -= 1
answer.reverse()
answer = ' '.join(map(str, answer))
print(answer)