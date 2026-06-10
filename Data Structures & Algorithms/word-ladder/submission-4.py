class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = {}
        for w in wordList+[beginWord]:
            adj[w] = []
            for w2 in wordList:
                diff = 0
                for c in range(len(w)):
                    if w[c] != w2[c]:
                        diff += 1
                    if diff > 1:
                        break
                if diff < 2:
                    adj[w].append(w2)
        q = deque([beginWord])
        visit = set()
        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word in visit:
                    continue
                visit.add(word)
                if word == endWord:
                    return res
                for nei in adj[word]:
                    q.append(nei)
        return 0

                