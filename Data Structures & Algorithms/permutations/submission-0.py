class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[nums[0]]]
        for n in range(1, len(nums)):
            new = []
            for p in res:
                temp = p
                for i in range(len(p)+1):
                    temp.insert(i, nums[n])
                    new.append(temp.copy())
                    temp.remove(nums[n])
            res = new
        return res

            