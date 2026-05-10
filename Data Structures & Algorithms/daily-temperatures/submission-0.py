class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        res = [0]*len(temperatures)

        for t in range(len(temperatures)):
            if not temps or temperatures[t] <= temperatures[temps[-1]]:
                temps.append(t)
            else:
                while temps and temperatures[t] > temperatures[temps[-1]]:
                    temp = temps.pop()
                    res[temp] = t-temp
                temps.append(t)
        return res