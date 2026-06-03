class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for c, p in prerequisites:
            if c == p:
                return False
            adj[c] = [p] + adj.get(c, [])
        complete = {}
        seen = set()
        def dfs(c):
            if c in complete:
                return complete[c]
            if c in seen:
                return False
            seen.add(c)
            possible = True
            for prereq in adj.get(c, []):
                if not dfs(prereq):
                    possible = False
                    break
            complete[c] = possible
            return complete[c]
        for c in range(numCourses):
            if not dfs(c):
                return False
        return len(complete) == numCourses

