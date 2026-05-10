class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0
        slow = nums[slow]
        fast = nums[fast]
        fast = nums[fast]
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
        slow2 = 0
        while nums[slow2] != nums[slow]:
            slow = nums[slow]
            slow2 = nums[slow2]
        return nums[slow]