class MedianFinder:

    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)

    def findMedian(self) -> float:
        if len(self.heap) == 0: return 0
        if len(self.heap) == 1: return self.heap[0]
        half = len(self.heap)//2
        if len(self.heap)%2 != 0:
            return list(heapq.nsmallest(half+1, self.heap))[-1]
        halfList = heapq.nsmallest(half+1, self.heap)
        return (list(halfList)[-1] + list(halfList)[-2])/2


        