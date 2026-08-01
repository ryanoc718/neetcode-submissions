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
            if not len(res) or c != res[-1]:
                count += 1
                res += c
                if count != 0:
                    cooldown.append([count, c])
            else:
                return ""
        return "" if len(cooldown) else res

