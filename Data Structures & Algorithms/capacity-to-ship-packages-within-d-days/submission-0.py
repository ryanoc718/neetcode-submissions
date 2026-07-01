class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap
                currCap -= w
            return True
        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            mid = (r+l)//2
            if canShip(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res
            