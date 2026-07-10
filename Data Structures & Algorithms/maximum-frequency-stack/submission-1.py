class FreqStack:

    def __init__(self):
        self.heap = []
        self.count = 0
        self.nums = {}
        

    def push(self, val: int) -> None:
        if val not in self.nums:
            self.nums[val] = 0
        self.nums[val] -= 1
        self.count -= 1
        heapq.heappush(self.heap, [self.nums[val], self.count, val])

    def pop(self) -> int:
        f, i, val = heapq.heappop(self.heap)
        self.nums[val] += 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()