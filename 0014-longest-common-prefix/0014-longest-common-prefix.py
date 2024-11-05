class Solution:
    def longestCommonPrefix(self, strs):
        op = ''
        min_val = min(len(word) for word in strs)

        for i in range(min_val):
            char = strs[0][i]

            if all(word[i] == char for word in strs):
                op += char
            else:
                break
        return op
        