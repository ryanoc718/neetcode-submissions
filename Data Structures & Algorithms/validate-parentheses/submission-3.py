class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for p in s:
            if p not in pairs:
                stack.append(p)
            elif len(stack) == 0:
                return False
            elif stack.pop() != pairs[p]:
                return False
            
        return len(stack) == 0