class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix)-1
        mid = (t+b)//2
        while t <= b:
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target and target < matrix[mid][-1]:
                break            
            if matrix[mid][0] > target:
                b = mid-1
            else:
                t = mid+1
            mid = (t+b)//2
        
        r = mid
        t, b = 0, len(matrix[mid])-1
        mid = (t+b)//2
        while t <= b:
            if matrix[r][mid] == target:
                return True
            if matrix[r][mid] > target:
                b = mid-1
            else:
                t = mid+1
            mid = (t+b)//2
        return False