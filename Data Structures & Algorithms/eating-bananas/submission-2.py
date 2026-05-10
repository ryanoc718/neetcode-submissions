class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        best = high
        while low <= high:
            k = (low+high)//2
            count = 0
            for p in piles:
                count += p//k + (0 if p%k==0 else 1)
            if count <= h:
                high = k-1
                best = min(best, k)
            else:
                low = k+1
        return best