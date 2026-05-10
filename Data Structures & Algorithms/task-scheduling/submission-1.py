class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1
        taskHeap = []
        for t, f in freq.items():
            taskHeap.append((-f, t))
        heapq.heapify(taskHeap)
        backlog = deque()
        time = 0
        while taskHeap or backlog:
            time += 1
            if len(backlog) > 0:
                count, task = backlog.popleft()
                if count < 0:
                    heapq.heappush(taskHeap, (count, task))
            if len(taskHeap) > 0:
                count, task = heapq.heappop(taskHeap)
                if count < -1:
                    while len(backlog) < n:
                        backlog.append((1, "IDLE"))
                    backlog.append((count+1, task))        
        return time
