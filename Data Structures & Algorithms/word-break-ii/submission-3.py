class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        sentence = []
        def dfs(i):
            if i == len(s):
                res.append(" ".join(sentence))
                return
            for word in wordDict:
                if i+len(word) <= len(s) and s[i:i+len(word)] == word:
                    sentence.append(word)
                    dfs(i+len(word))
                    sentence.pop()
        dfs(0)
        return res
