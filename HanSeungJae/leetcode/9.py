class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        return True if strX == strX[::-1] else False
