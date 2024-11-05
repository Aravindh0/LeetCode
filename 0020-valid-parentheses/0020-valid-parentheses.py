class Solution:
    def isValid(self, s):
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in brackets:
                stack.append(i)
            else:
                elem = stack.pop() if stack else '#'
                if i != brackets.get(elem):
                    return False
                    break
        return len(stack) == 0
