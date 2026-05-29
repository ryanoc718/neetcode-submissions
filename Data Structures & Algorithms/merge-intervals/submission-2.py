class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        start, end = intervals[0][0], intervals[0][1]
        for s, e in intervals:
            if end < s:
                res.append([start, end])
                start = s
                end = e
            else:
                end = max(end, e)
        res.append([start, end])
        return res

