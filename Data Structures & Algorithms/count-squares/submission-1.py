class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        x, y = point
        if (x, y) not in self.points:
            self.points[(x, y)] = 0
        self.points[(x, y)] += 1       

    def count(self, point: List[int]) -> int:
        count = 0
        x, y = point
        for nx, ny in self.points:
            if x-nx != 0 and y-ny != 0:
                if (x, ny) in self.points and (nx, y) in self.points:
                    count += (self.points.get((x,y), 1) * self.points[(nx, ny)] *
                    self.points[(x, ny)] * self.points[(nx, y)])
        return count




        
