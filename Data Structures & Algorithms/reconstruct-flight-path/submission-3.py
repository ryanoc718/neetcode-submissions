class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        for s, d in tickets:
            adj[s] = adj.get(s, []) + [d]
        path = []
        def dfs(loc):
            if len(path) == len(tickets)+1:
                return True
            if len(path) > len(tickets)+1:
                return False
            for dest in sorted(adj.get(loc, [])):
                path.append(dest)
                adj[loc].remove(dest)
                if dfs(dest):
                    return True
                adj[loc].append(dest)
                path.pop()
            return False
        path.append("JFK")
        dfs("JFK")
        return path

            
            
