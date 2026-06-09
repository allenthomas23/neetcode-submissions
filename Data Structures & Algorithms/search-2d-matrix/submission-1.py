class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows,cols = len(matrix), len(matrix[0])
        l,r=0,rows-1
        while l<=r:
            row = (l+r)//2
            if matrix[row][-1] <target:
                l = row+1
            elif matrix[row][0] > target:
                r = row -1
            else:
                break

        if not (l <= r):
            return False
        row = (l+r)//2
        l,r =0,cols -1
        while(l<=r):
            mid = (l+r)//2 
            if matrix[row][mid] <target:
                l = mid+1
            elif matrix[row][mid] > target:
                r = mid -1
            else:
                return True

        return False
                    
