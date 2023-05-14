class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st, tmp, result = 0, "", ""

        for i in range(0, len(s)):
            idx = tmp.find(s[i])
            if idx != -1:
                st += idx + 1
            tmp = s[st : i + 1]
            result = max(result, tmp, key=lambda x: len(x))

        return len(result)
