class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            one, two = heapq.heappop(stones), heapq.heappop(stones)
            if one - two < 0:
                heapq.heappush(stones, one-two)
        return -1*stones[0] if len(stones) > 0 else 0
