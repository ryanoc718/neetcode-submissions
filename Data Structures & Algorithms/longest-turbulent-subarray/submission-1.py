class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        best = 1
        curr = 1
        i = 0
        sign = "<"
        while i < len(arr)-1:
            if curr == 1:
                sign = "<" if arr[i] < arr[i+1] else ">"
            if sign == "<":
                if arr[i] < arr[i+1]:
                    curr += 1
                    sign = ">"
                    i += 1
                else:
                    curr = 1
                    sign = "<"
                    if arr[i] == arr[i+1]:
                        i += 1
            else:
                if arr[i] > arr[i+1]:
                    curr += 1
                    i += 1
                else:
                    curr = 1
                    if arr[i] == arr[i+1]:
                        i += 1
                sign = "<"
            best = max(best, curr)
        return best
                    

