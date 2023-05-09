class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i1, n1 in enumerate(nums):
            for i2, n2 in enumerate(nums[i1 + 1 :]):
                if n1 + n2 == target:
                    return [i1, i1 + 1 + i2]
