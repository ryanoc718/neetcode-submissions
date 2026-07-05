class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l, r = 0, mountainArr.length()-1
        peak = 0
        while l <= r:
            mid = (l+r)//2
            leftVal, rightVal = mountainArr.get(mid-1), mountainArr.get(mid+1)
            midVal = mountainArr.get(mid) 
            if midVal > leftVal and midVal > rightVal :
                peak = mid
                break
            if leftVal <= midVal:
                l = mid+1
            else:
                r = mid-1
        l, r = 0, peak
        while l <= r:
            mid = (l+r)//2
            leftVal, rightVal = mountainArr.get(l), mountainArr.get(r)
            midVal = mountainArr.get(mid)
            if midVal == target:
                return mid
            if midVal > target:
                r = mid-1
            else:
                l = mid+1
        l, r = peak+1, mountainArr.length()-1
        while l <= r:
            mid = (l+r)//2
            leftVal, rightVal = mountainArr.get(l), mountainArr.get(r)
            midVal = mountainArr.get(mid)
            if midVal == target:
                return mid
            if midVal > target:
                l = mid+1
            else:
                r = mid-1
        return -1










