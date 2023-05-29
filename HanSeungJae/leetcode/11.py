class Solution:
    def maxArea(self, height: List[int]) -> int:
        N, answer = len(height) - 1, 0

        l, r = 0, N
        while l < r:
            answer = max(answer, (r - l) * min(height[l], height[r]))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return answer
