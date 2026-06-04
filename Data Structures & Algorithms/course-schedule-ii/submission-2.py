class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for c, p in prerequisites:
            adj[c] = [p] + adj.get(c, [])
        order = []
        validated = set()
        seen = set()
        def dfs(crs):
            if crs in seen:
                return False
            if crs in validated:
                return True
            seen.add(crs)
            for pr in adj.get(crs, []):
                if not dfs(pr):
                    return False
            seen.remove(crs)
            order.append(crs)
            validated.add(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return order
        