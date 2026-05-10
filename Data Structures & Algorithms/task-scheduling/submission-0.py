class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = {}
        for t in tasks:
            freqs[t] = freqs.get(t, 0) + 1
        heap = [[-f, t] for t, f in freqs.items()]
        heapq.heapify(heap)

        output = []
        dq = deque()

        while heap or dq:
            if dq:
                t = dq.popleft()
                if t != "IDLE":
                    heapq.heappush(heap, t)
            if heap:
                count, task = heapq.heappop(heap)
                count += 1
                output.append(task)

                if count < 0:
                    while len(dq) < n:
                        dq.append("IDLE")
                    dq.append([count, task])
            else:
                output.append("IDLE")
        return len(output)





