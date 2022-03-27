def get_max_value_case(K):
    dp = [0] * (K + 1)
    for w, v in WV:
        for i in range(K, -1, -1):
            if i-w < 0:
                break
            dp[i] = max(dp[i-w]+v, dp[i])

    return dp[K]


N, K = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]
WV.sort()

print(get_max_value_case(K))