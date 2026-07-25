class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-1
        while l <= r:
            mid = (r+l)//2
            if arr[mid] == x:
                l = mid+1
                break
            if arr[mid] < x:
                l = mid+1
            else:
                r = mid-1
        l, r = l-1, l
        res = []
        while len(res) < k:
            if l < 0:
                res.append(arr[r])
                r += 1
            elif r == len(arr):
                res = [arr[l]] + res
                l -= 1
            elif abs(arr[l]-x) <= abs(arr[r]-x):
                res = [arr[l]] + res
                l -= 1
            else:
                res.append(arr[r])
                r += 1
        return res
