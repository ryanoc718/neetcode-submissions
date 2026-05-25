class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')' and len(stack):
                stack.pop()
            elif c == ')' and len(stars):
                stars.pop()
            elif c == ')':
                return False
            else:
                stars.append(i)  
        while len(stack) and len(stars):
            if stack[-1] < stars[-1]:
                stack.pop()
                stars.pop()
            else:
                return False
        return not len(stack)
            
            
