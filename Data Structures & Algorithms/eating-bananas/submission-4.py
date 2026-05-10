class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high
        while low <= high:
            mid = (low+high)//2
            time = 0
            for p in piles:
                if p%mid == 0:
                    time += p/mid
                else:
                    time += p//mid + 1
            if time <= h:
                res = min(res, mid)
                high = mid-1
            else:
                low = mid+1
        return res