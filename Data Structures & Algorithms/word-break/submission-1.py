class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def WB(s, wordDict, memo):
            if len(s) == 0:
                return True
            if s in memo:
                return False
            memo.add(s)
            for c in range(len(s)):
                if s[:c+1] in wordDict and WB(s[c+1:], wordDict, memo):
                    return True
            return False
        return WB(s, wordDict, set())
        
            
                