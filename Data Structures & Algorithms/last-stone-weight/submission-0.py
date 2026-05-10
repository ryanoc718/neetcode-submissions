class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            remains = y - x
            if remains:
                heapq.heappush(stones, remains)

        return stones[0]*-1 if len(stones) else 0 