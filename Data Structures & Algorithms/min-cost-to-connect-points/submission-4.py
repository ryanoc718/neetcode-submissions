class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}
        for i in range(len(points)):
            adj[i] = []
        for i in range(0, len(points)):
            for j in range(i+1, len(points)):
                dist = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        heap = [(0,0)]
        visit = set()
        total = 0
        while heap:
            cost, p = heapq.heappop(heap)
            if p in visit:
                continue
            visit.add(p)
            total += cost
            if len(visit) == len(points):
                return total
            for cost, nei in adj[p]:
                if nei not in visit:
                    heapq.heappush(heap, (cost, nei))


