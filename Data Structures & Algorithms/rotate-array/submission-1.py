class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        cycleStart = -1
        while count < len(nums):
            cycleStart += 1
            curIdx = -1
            cur = nums[cycleStart]
            while curIdx != cycleStart:
                curIdx = cycleStart if curIdx == -1 else curIdx
                count += 1
                temp = nums[(curIdx+k)%len(nums)]
                nums[(curIdx+k)%len(nums)] = cur
                cur = temp
                curIdx = (curIdx+k)%len(nums)



        