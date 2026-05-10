class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trips = set()
        sortedNums = sorted(nums)
        for i in range(0, len(sortedNums)-2):
            j,k = i+1, len(sortedNums)-1
            while j < k:
                if sortedNums[i]+sortedNums[j]+sortedNums[k] > 0:
                    k -= 1 
                elif sortedNums[i]+sortedNums[j]+sortedNums[k] < 0:
                    j += 1
                elif sortedNums[i]+sortedNums[j]+sortedNums[k] == 0:
                    trips.add(tuple([sortedNums[i],sortedNums[j],sortedNums[k]]))
                    k -= 1
        result = []
        for t in trips:
            result.append(list(t))
        return result