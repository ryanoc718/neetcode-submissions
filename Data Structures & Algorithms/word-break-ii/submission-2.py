class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        memo = {}
        def dfs(i, sentence):
            if i == len(s):
                res.append(sentence)
                return
            for word in wordDict:
                if i+len(word) <= len(s) and s[i:i+len(word)] == word:
                    space = ""
                    if len(sentence):
                        space = " "
                    dfs(i+len(word), sentence+space+word)
        dfs(0, "")
        return res
