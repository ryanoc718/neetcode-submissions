class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for point in points:
            x, y = point[0], point[1]
            distance = abs(((x*x)+(y*y))**0.5)
            heapq.heappush(heap, [-1*distance, point])
            if len(heap) > k:
                heapq.heappop(heap)

        res = [p[1] for p in heap]
        return res
