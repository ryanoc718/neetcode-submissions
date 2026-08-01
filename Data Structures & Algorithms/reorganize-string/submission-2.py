class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) - 1
        heap = []
        for c in counts:
            heapq.heappush(heap, [counts[c], c])
        res = ""
        cooldown = None
        while heap:
            count, c = heapq.heappop(heap)
            if cooldown:
                heapq.heappush(heap, cooldown)
                cooldown = None
            count += 1
            res += c
            if count != 0:
                cooldown = [count, c]
        return "" if cooldown else res

