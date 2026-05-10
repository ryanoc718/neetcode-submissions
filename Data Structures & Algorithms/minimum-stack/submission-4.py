class MinStack:

    def __init__(self):
        self.stack = []
        self.minVals = []

    def push(self, val: int) -> None:
        if not self.stack or val < self.minVals[-1]:
            self.minVals.append(val)
        else:
            self.minVals.append(self.minVals[-1])
        self.stack.append(val)

    def pop(self) -> None:
        self.minVals.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVals[-1]