class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.cap = capacity
        self.dynamicArray = [None]*capacity

    def get(self, i: int) -> int:
        return self.dynamicArray[i]

    def set(self, i: int, n: int) -> None:
        self.dynamicArray[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.cap:
            self.resize()
        self.dynamicArray[self.size] = n
        self.size += 1

    def popback(self) -> int:
        pop = self.dynamicArray[self.size-1]
        self.dynamicArray[self.size-1] = None
        self.size -= 1
        return pop

    def resize(self) -> None:
        self.dynamicArray += [None]*self.cap
        self.cap *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.cap