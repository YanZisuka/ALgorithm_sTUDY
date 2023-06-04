class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        r = min(len(str) for str in strs)
        isCommon = True
        for i in range(r):
            cs = [str[i] for str in strs]
            for i in range(len(cs) - 1):
                c, nc = cs[i], cs[i + 1]
                if c != nc:
                    isCommon = False
                    break
            if isCommon:
                prefix += cs[0]

        return prefix


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))  # 'fl'
print(s.longestCommonPrefix(["dog", "racecar", "car"]))  # ''
