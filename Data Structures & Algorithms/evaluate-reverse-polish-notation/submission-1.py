class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            if t == '+':
                if len(nums):
                    right = int(nums.pop())
                if len(nums):
                    left = int(nums.pop())
                nums.append(left+right)
            elif t == '-':
                if len(nums):
                    right = int(nums.pop())
                if len(nums):
                    left = int(nums.pop())
                nums.append(left-right)
            elif t == '*':
                if len(nums):
                    right = int(nums.pop())
                if len(nums):
                    left = int(nums.pop())
                nums.append(left*right)
            elif t == '/':
                if len(nums):
                    denom = int(nums.pop())
                if len(nums):
                    num = int(nums.pop())
                nums.append(int(num/denom))
            else:
                nums.append(int(t))
        return nums[-1]