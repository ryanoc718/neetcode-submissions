class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        mid = (l+r)//2
        row = 0
        while l <= r:
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target <= matrix[mid][len(matrix[mid])-1]:
                row = mid
                break
            elif matrix[mid][0] > target:
                r = mid-1
            else:
                l = mid+1
            mid = (l+r)//2
        l, r = 0, len(matrix[row])-1
        mid = (l+r)//2
        while l <= r:
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid-1
            else:
                l = mid+1
            mid = (l+r)//2
        return False
                
        
