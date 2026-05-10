class MinStack:

    def __init__(self):
        self.stack = []
        self.minList = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.minList.append(val)
        elif val <= self.minList[-1]:
            self.minList.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.minList[-1] == self.stack[-1]:
            self.minList = self.minList[:(len(self.minList)-1)]
        self.stack = self.stack[:len(self.stack)-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minList[-1]