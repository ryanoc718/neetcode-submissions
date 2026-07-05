class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        farthest = 0
        for p, s, d in trips:
            farthest = max(farthest, d)
        locs = [0]*(farthest+1)
        for p, s, d in trips:
            for i in range(s, d):
                locs[i] += p
        for i in range(len(locs)):
            if locs[i] > capacity:
                return False
        return True