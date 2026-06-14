class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = 0, 0
        for i in range(len(cost)):
            temp = one
            one = cost[i] + min(one, two)
            two = temp
        return min(one, two)