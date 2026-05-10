class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in range(len(nums)):
            newLists = []
            for l in res:
                newLists.append(l+[nums[n]])
            res += newLists
        return res