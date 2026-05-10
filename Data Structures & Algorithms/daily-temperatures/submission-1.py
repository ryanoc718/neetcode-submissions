class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        res = [0]*len(temperatures)
        for t in range(len(temperatures)):
            while len(temps) and temperatures[t] > temperatures[temps[-1]]:
                res[temps[-1]] = t-temps[-1]
                temps.pop()
            temps.append(t)
        return res

