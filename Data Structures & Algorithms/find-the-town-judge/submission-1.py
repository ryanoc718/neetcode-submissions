class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        seen = defaultdict(int)
        trusts = set()
        for p, t in trust:
            seen[t] += 1
            trusts.add(p)
        judge = trust[0][1]
        for p in seen:
            if seen[p] == n-1 and p not in trusts:
                return p
        return -1

        

