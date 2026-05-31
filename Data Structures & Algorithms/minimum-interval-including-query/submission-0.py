class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for q in queries:
            shortest = float("inf")
            for s, e in intervals:
                if s <= q <= e:
                    shortest = min(shortest, (e-s)+1)
            if shortest == float("inf"):
                shortest = -1
            res.append(shortest)
        return res