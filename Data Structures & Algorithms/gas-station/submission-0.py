class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            g = 0
            for j in range(i, i+len(gas)+1):
                if j >= len(gas):
                    if j == i+len(gas):
                        return i
                    g += gas[j-len(gas)]
                    g -= cost[j-len(gas)]
                    if g < 0:
                        break
                else:
                    if j == i+len(gas):
                        return i
                    g += gas[j]
                    g -= cost[j]
                    if g < 0:
                        break
        return -1
                
