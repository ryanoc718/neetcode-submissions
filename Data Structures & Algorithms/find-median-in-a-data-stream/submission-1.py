class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)
        self.median = 0

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == 0 and len(self.maxHeap) == 0:
            self.median = num
            heapq.heappush(self.maxHeap, num)
            return
        elif num <= self.median:
            heapq.heappush(self.minHeap, -num)
            while len(self.minHeap) > len(self.maxHeap)+1:
                val = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -val)
        else:
            heapq.heappush(self.maxHeap, num)
            while len(self.minHeap)+1 < len(self.maxHeap):
                val = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, -val)
        
        if len(self.minHeap) == len(self.maxHeap):
            self.median = ((self.minHeap[0]*-1)+self.maxHeap[0])/2
        elif len(self.minHeap) > len(self.maxHeap):
            self.median = self.minHeap[0]*-1
        else:
            self.median = self.maxHeap[0]


    def findMedian(self) -> float:
        return self.median


        