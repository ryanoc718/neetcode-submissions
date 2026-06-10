class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = {}
        visited = {}
        for w in wordList+[beginWord]:
            adj[w] = []
            visited[w] = float("inf")
            for w2 in wordList:
                if w == w2:
                    continue
                diff = 0
                for c in range(len(w)):
                    if w[c] != w2[c]:
                        diff += 1
                    if diff > 1:
                        break
                if diff < 2:
                    adj[w].append(w2)
        seen = set()
        def dfs(word, count):
            if visited[word] < count:
                return float("inf")
            visited[word] = count
            if word == endWord:
                return count
            best = float("inf")
            seen.add(word)
            for nei in adj[word]:
                if nei not in seen:
                    best = min(dfs(nei, count+1), best)
            seen.remove(word)
            return best
        res = dfs(beginWord, 0)
        return res+1 if res != float("inf") else 0






