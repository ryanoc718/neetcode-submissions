class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.keys:
            return ""
        recent = ""
        l, r = 0, len(self.keys[key])-1
        while l <= r:
            mid = (l+r)//2
            if self.keys[key][mid][0] == timestamp:
                return self.keys[key][mid][1]
            if self.keys[key][mid][0] < timestamp:
                recent = self.keys[key][mid][1]
                l = mid+1
            else:
                r = mid-1
        return recent





