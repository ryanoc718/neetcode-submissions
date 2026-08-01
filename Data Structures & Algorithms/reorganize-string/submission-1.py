class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) - 1
        heap = []
        for c in counts:
            heapq.heappush(heap, [counts[c], c])
        res = ""
        cooldown = []
        while heap:
            count, c = heapq.heappop(heap)
            if len(cooldown):
                heapq.heappush(heap, cooldown.pop())
            count += 1
            res += c
            if count != 0:
                cooldown.append([count, c])
        return "" if len(cooldown) else res

