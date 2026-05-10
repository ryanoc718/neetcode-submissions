class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                x, y = stack.pop(), stack.pop()
                stack.append(x+y)
            elif t == '-':
                x, y = stack.pop(), stack.pop()
                stack.append(y-x)
            elif t == '*':
                x, y = stack.pop(), stack.pop()
                stack.append(x*y)
            elif t == '/':
                x, y = stack.pop(), stack.pop()
                if y%x == 0:
                    stack.append(y//x)
                elif y//x < 0:
                    stack.append(int(y//x)+1)
                else: stack.append(int(y//x))
            else:
                stack.append(int(t))
        return stack[-1]