class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, combo, total):
            if total == target:
                res.append(combo.copy())
                return
            if i == len(nums) or total > target:
                return
            backtrack(i+1, combo, total)
            backtrack(i, combo+[nums[i]], total+nums[i])
        backtrack(0,[],0)
        return res

