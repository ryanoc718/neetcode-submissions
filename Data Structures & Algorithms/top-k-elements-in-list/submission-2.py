class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1

        freqs = sorted(counts.values(), reverse=True)
        minFreq = freqs[k-1]

        finalists = []
        for key in counts:
            if counts[key] >= minFreq:
                finalists.append(key)
        return finalists