class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        left = [0]*len(height)
        right = [0]*len(height)
        for i in range(len(height)):
            if i > 0:
                left[i] = max(left[i-1], height[i-1])
        for i in range(len(height)-1, -1, -1):
            if i < len(height)-1:
                right[i] = max(right[i+1], height[i+1])
        vol = 0
        for i in range(len(height)):
            top = min(left[i], right[i])
            if top-height[i] > 0:
                vol += (top-height[i])
        return vol
