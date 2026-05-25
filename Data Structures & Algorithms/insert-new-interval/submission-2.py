class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = 0, len(intervals)-1
        mid = (r+l)//2
        inserted = False
        while l <= r:
            if intervals[mid][0] == newInterval[0]:
                intervals.insert(mid, newInterval)
                inserted = True
                break
            elif intervals[mid][0] > newInterval[0]:
                r = mid-1
            else:
                l = mid+1
            mid = (r+l)//2
        
        if not inserted:
            intervals.insert(l, newInterval)
        new = []
        start, end = -1, -1
        for i in intervals:
            if i[0] > end:
                start = i[0]
                end = i[1]
                new.append([start, end])
            else:
                end = max(end, i[1])
                new[-1][1] = end
        return new



