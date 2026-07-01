class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counts = {}
        for n in hand:
            counts[n] = counts.get(n, 0) +1
        heap = []
        for v, c in counts.items():
            heapq.heappush(heap, [v, c])
        while heap:
            group = []
            for _ in range(groupSize):
                if not heap:
                    return False
                v, c = heapq.heappop(heap)
                if len(group) == 0 or v == 1+group[-1][0]:
                    group.append([v, c-1])
                else:
                    return False
            for v, c in group:
                if c != 0:
                    heapq.heappush(heap, [v, c])
        return True
