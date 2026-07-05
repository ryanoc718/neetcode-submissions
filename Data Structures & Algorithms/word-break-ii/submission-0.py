class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wd = set(wordDict)
        def dfs(i, sentence):
            if i == len(s):
                output = " ".join(sentence)
                res.append(output)
                return
            for j in range(i+1, len(s)+1):
                if s[i:j] in wd:
                    sentence.append(s[i:j])
                    dfs(j, sentence)
                    sentence.pop()
        dfs(0, [])
        return res
