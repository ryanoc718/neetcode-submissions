class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        L = len(heights)
        left, right = [0]*L, [L-1]*L
        stack = []
        for i in range(L):
            if not stack or heights[i] > heights[stack[-1]]:
                left[i] = stack[-1] if stack else -1
                stack.append(i)
            else:
                while stack and heights[i] <= heights[stack[-1]]:
                    stack.pop()
                left[i] = stack[-1] if stack else -1
                stack.append(i) 
        stack = []
        for i in range(L-1, -1, -1):
            if not stack or heights[i] > heights[stack[-1]]:
                right[i] = stack[-1] if stack else L
                stack.append(i)
            else:
                while stack and heights[i] <= heights[stack[-1]]:
                    stack.pop()
                right[i] = stack[-1] if stack else L
                stack.append(i) 
        res = 0
        for i in range(L):
            res = max(res, heights[i]*(right[i]-left[i]-1))
        return res