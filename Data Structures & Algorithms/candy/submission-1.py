class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1]*len(ratings)
        low = min(ratings)
        for i, r in enumerate(ratings):
            if i > 0 and r > ratings[i-1]:
                res[i] = 1 + res[i-1]
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1] and res[i] <= res[i+1]:
                res[i] = 1 + res[i+1]
        print(res)
        return sum(res)
        