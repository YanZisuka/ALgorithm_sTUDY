class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True

        for i in range(2, len(p) + 1):
            if p[i - 1] == "*":
                dp[0][i] = dp[0][i - 2]

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] == s[j - 1] or p[i - 1] == ".":
                    dp[j][i] = dp[j - 1][i - 1]
                elif p[i - 1] == "*":
                    dp[j][i] = dp[j][i - 2]
                    if p[i - 2] == s[j - 1] or p[i - 2] == ".":
                        dp[j][i] = dp[j][i] or dp[j - 1][i]

        return dp[-1][-1]
