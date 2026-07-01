class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counts = {}
        for n in hand:
            counts[n] = counts.get(n, 0) +1
        heap = []
        for v in counts:
            heapq.heappush(heap, v)
        while heap:
            group = []
            for _ in range(groupSize):
                if not heap:
                    return False
                v = heapq.heappop(heap)
                if len(group) == 0 or v == 1+group[-1]:
                    group.append(v)
                else:
                    return False
            for v in group:
                counts[v] -= 1
                if counts[v] != 0:
                    heapq.heappush(heap, v)
        return True
