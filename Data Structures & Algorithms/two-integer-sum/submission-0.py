class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(0, len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = i
            if target-nums[i] in seen and seen[target-nums[i]] != i:
                return [seen[target-nums[i]], i]
        return [0,1]
