class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = {}
        for a in accounts:
            for email in range(1, len(a)):
                adj[a[email]] = a[1:] + adj.get(a[email], [])
        seen = set()
        def dfs(email):
            if email in seen:
                return
            seen.add(email)
            newgroup.append(email)
            for nei in adj[email]:
                dfs(nei)
        res = []
        for account in accounts:
            newgroup = [account[0]]
            dfs(account[1])
            if len(newgroup) > 1:
                res.append(newgroup)
        return res

            