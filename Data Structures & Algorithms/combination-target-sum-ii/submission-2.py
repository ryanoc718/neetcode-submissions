class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(subset, idx, total):
            if total == target:
                res.append(subset.copy())
                return
            if idx >= len(candidates) or total > target:
                return
            subset.append(candidates[idx])
            total += candidates[idx]
            backtrack(subset, idx+1, total)
            subset.pop()
            total -= candidates[idx]
            while idx < len(candidates)-1 and candidates[idx] == candidates[idx+1]:
                idx += 1
            backtrack(subset, idx+1, total)
        backtrack([], 0, 0)
        return res