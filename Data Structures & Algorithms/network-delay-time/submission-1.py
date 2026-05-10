class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n+1)}
        for u,v,t in times:
            adj[u].append([t,v])
        h = [[0, k]]
        seen = set()
        res = 0
        while len(h) and len(seen) < n:
            time, node = heapq.heappop(h)
            if node in seen:
                continue
            seen.add(node)
            res = time
            for t, v in adj[node]:
                t += res
                heapq.heappush(h, [t, v])
        return res if len(seen) == n else -1
