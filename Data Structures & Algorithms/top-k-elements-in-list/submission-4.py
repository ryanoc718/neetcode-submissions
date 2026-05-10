class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        heap = [[f, v] for v, f in freq.items()]
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        res = [v for f, v in heap]
        return res