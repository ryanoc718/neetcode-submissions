class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n+1):
            adj[i] = []
        for u, v, t in times:
            adj[u].append((t,v))
        heap = [(0, k)]
        res = 0
        seen = set()
        while heap:
            for _ in range(len(heap)):
                t, u = heapq.heappop(heap)
                if u in seen:
                    continue
                res = max(t, res)
                seen.add(u)
                for d, v in adj[u]:
                    heapq.heappush(heap, (t+d, v))
        return res if len(seen) == n else -1

