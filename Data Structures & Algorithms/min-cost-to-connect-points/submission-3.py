class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}
        for x, y in points:
            adj[(x, y)] = []
            for x2, y2 in points:
                if (x,y) != (x2, y2):
                    adj[(x, y)].append((abs(x-x2)+abs(y-y2), (x2, y2)))
        total = 0
        heap = [(0, (points[0][0], points[0][1]))]
        seen = set()
        while heap:
            cost, c = heapq.heappop(heap)
            if (c[0], c[1]) in seen:
                continue
            seen.add((c[0], c[1]))
            total += cost
            if len(seen) == len(points):
                return total
            for dist, nei in adj[(c[0], c[1])]:
                if (nei[0], nei[1]) not in seen:
                    heapq.heappush(heap, (dist, (nei[0], nei[1])))
        return total

