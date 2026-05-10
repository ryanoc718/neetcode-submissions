class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prs = {}
        for i in range(numCourses):
            prs[i] = []
        for c, p in prerequisites:
            prs[c].append(p)
        visited = set()
        res = []
        resSet = set()
        def dfs(c):
            if c in visited:
                return False
            visited.add(c)
            for p in prs[c]:
                if not dfs(p): return False
            visited.remove(c)
            prs[c] = []
            if c not in resSet: res.append(c)
            resSet.add(c)
            return True
        for c in range(numCourses):
            if not dfs(c): return []
            
        return res



        