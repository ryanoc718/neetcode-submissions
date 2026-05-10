class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []

        for p in s:
            if p not in pairs:
                stack.append(p)
            elif stack and stack[-1] == pairs[p]:
                stack.pop()
            else:
                return False
        return len(stack) == 0