class Solution:
    def romanToInt(self, s: str):
        a = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        val = 0
        prev_val = 0
        for i in s:
            current_val = a[i]
            if current_val > prev_val:
                val += current_val - 2 * prev_val
            else:
                val += current_val
            prev_val = current_val
        return val
        