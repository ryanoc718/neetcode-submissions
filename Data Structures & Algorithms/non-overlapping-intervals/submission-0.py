class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        start, end = intervals[0][0], intervals[0][1]
        remove = -1
        for s, e in intervals:
            if end > s:
                remove += 1
                if end > e:
                    end = e
                    start = s
            else:
                end = e
                start = s
        return remove

