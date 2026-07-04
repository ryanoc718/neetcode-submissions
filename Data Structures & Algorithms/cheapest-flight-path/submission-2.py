class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for s, d, p in flights:
            adj[s].append([p, d])

        heap = [[0, src, k]]
        while heap:
                cost, src, k = heapq.heappop(heap)
                if src == dst:
                    return cost
                if k < 0:
                    continue
                k -= 1
                for p, d in adj.get(src, []):
                    heapq.heappush(heap, [cost+p, d, k])
        return -1

        