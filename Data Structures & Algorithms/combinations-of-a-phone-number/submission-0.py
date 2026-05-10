class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        digitMap = {2: "abc", 3: "def", 4: "ghi", 5: "jkl",
        6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        res = []

        def backtrack(combo, digitIdx, l):
            print(combo)
            if len(combo) == len(digits):
                res.append(combo[:])
                return
            if digitIdx >= len(digits):
                return
            for c in digitMap[int(digits[digitIdx])]:
                update = combo+c
                backtrack(update[:], digitIdx+1, l)            
        for c in digitMap[int(digits[0])]: 
            backtrack(c, 1, 0)
        return res
            