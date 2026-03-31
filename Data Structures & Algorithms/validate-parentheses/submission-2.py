class Solution:
    def isValid(self, s: str) -> bool:
        opening_brackets = {'(':')', '{':'}','[': ']'}
        stack = []
        for i in s:
            if i in opening_brackets:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                l = stack[-1]
                if i != opening_brackets[l]:
                    return False
                stack.pop()
        return len(stack) == 0
