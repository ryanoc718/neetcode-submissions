class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(i, combo, total):
            if total == target:
                res.append(combo.copy())
                return
            if i == len(candidates) or target < total:
                return
            combo.append(candidates[i])
            backtrack(i+1, combo, total + candidates[i])
            combo.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, combo, total)
        backtrack(0, [], 0)
        return res
