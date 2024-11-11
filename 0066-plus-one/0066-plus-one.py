class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = int(''.join(map(str, digits)))
        a += 1
        res = []
        for i in str(a):
            res.append(int(i))
        return res
