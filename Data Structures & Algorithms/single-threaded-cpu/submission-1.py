class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        timeHeap = []
        procHeap = []
        for i, t in enumerate(tasks):
            heapq.heappush(timeHeap, [t[0], t[1], i])
        res = []
        time = 0
        while timeHeap or procHeap:
            while timeHeap and timeHeap[0][0] <= time:
                e, p, i = heapq.heappop(timeHeap)
                heapq.heappush(procHeap, [p, i])
            if procHeap:
                p, i = heapq.heappop(procHeap)
                time += p
                res.append(i) 
            else:
                time = timeHeap[0][0]
        return res

        
