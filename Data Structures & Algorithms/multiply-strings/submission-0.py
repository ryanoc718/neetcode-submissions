class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        nums = {str(i):i for i in range(10)}
        ten = 0
        one = 0
        for i in range(len(num1)-1, -1, -1):
            one += nums[num1[i]]*(10**ten)
            ten += 1
        ten = 0
        two = 0
        for i in range(len(num2)-1, -1, -1):
            two += nums[num2[i]]*(10**ten)
            ten += 1
        return str(one*two)