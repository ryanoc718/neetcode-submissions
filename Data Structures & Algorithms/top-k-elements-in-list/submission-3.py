class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fDict = {}
        fList = [[] for _ in range(len(nums))]
        for n in nums:
            fDict[n] = fDict.get(n, 0)+1
        for key in fDict:
            fList[fDict[key]-1].append(key)
        res = []
        for n in range(len(fList)-1, -1, -1):
            if len(res) == k:
                return res
            for v in fList[n]:
                res.append(v)
        return res
