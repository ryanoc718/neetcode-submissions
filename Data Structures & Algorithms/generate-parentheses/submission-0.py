class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(o, c, para, stack):
            if o <= 0 and c <= 0:
                res.append(para[:])
                return
            if o:
                para += "("
                o -= 1
                stack.append("(")
                dfs(o, c, para, stack.copy())
                stack.pop()
                para = para[:-1]
                o += 1
            if c and stack and stack[-1] == "(": 
                para += ")"
                stack.pop()
                c -= 1
                dfs(o, c, para, stack.copy())
        dfs(n-1, n, "(", ["("])
        return res

