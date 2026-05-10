class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        edges = {w:[] for w in wordList}
        edges[beginWord], edges[endWord] = [], []
        for word in wordList:
            for node in edges:
                if node == word:
                    continue
                diff = 0
                for c in range(len(word)):
                    if word[c] != node[c]:
                        diff += 1
                    if diff > 1:
                        break
                if diff == 1:
                    edges[node].append(word)
        shortest = len(wordList)+1
        def dfs(word, seen, path):
            nonlocal shortest
            path += 1
            if word == endWord:
                shortest = min(shortest, path)
            if word in seen or path >= shortest:
                return
            seen.add(word)
            for nei in edges[word]:
                dfs(nei, seen, path)
            seen.remove(word)
        dfs(beginWord, set(), 0)
        return shortest if shortest <= len(wordList) else 0








