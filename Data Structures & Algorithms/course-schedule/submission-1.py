class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {}
        for i in range(numCourses):
            prereqs[i] = []
        for c, p in prerequisites:
            prereqs[c] = [p] + prereqs.get(c, [])
        
        visited = set()
        def dfs(c):
            if c in visited:
                return False
            
            visited.add(c)
            for req in prereqs[c]:
                if not dfs(req):
                    return False
            prereqs[c] = []
            visited.remove(c)
            return True
        for course in prereqs:
            if not dfs(course):
                return False
        return True
