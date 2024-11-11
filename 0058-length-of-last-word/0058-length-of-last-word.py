class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = len(s.strip().split(' ')[-1])
        return res