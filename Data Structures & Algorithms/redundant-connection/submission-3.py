class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = 1
        for edge in edges:
            if edge[-1] > N:
                N = edge[-1]
        adj = {i:[] for i in range(1, N+1)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        seen = set()
        def dfs(parent, node):
            if node in seen:
                return
            seen.add(node)
            if len(adj[node]) == 1:
                adj[adj[node][0]].remove(node)
                del adj[node]
                return
            for nei in adj[node]:
                if nei != parent:
                    dfs(node, nei)
        loopDetected = False
        while not loopDetected:
            loopDetected = True
            for i in range(1, N+1):
                if i in adj and len(adj[i]) == 1:
                    loopDetected = False
                    adj[adj[i][0]].remove(i)
                    del adj[i]
                elif i in adj:
                    seen.clear()
                    dfs(-1, i)
        
        for a,b in edges[::-1]:
            if a in adj and b in adj[a]:
                return [a,b]
        return [0,0]
            



        