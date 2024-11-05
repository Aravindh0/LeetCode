class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
            
        org = x
        reverse = 0
        while x > 0:
            remainder = x % 10
            reverse = (reverse * 10) + remainder
            x //= 10
        return org == reverse