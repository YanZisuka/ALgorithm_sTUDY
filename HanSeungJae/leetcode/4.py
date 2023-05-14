class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        INF = float("inf")

        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        partitionLen = (len(nums1) + len(nums2) + 1) // 2
        isOdd = (len(nums1) + len(nums2)) % 2 == 1

        st, en = 0, len(nums1)
        while st <= en:
            nums1Idx = (st + en) // 2
            nums2Idx = partitionLen - nums1Idx

            maxLeft1 = nums1[nums1Idx - 1] if nums1Idx != 0 else -INF
            minRight1 = nums1[nums1Idx] if nums1Idx != len(nums1) else INF

            maxLeft2 = nums2[nums2Idx - 1] if nums2Idx != 0 else -INF
            minRight2 = nums2[nums2Idx] if nums2Idx != len(nums2) else INF

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                return (
                    max(maxLeft1, maxLeft2)
                    if isOdd
                    else (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                )
            elif maxLeft1 > minRight2:
                en = nums1Idx - 1
            else:
                st = nums1Idx + 1
