class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            l,r =0,len(row) -1
            mid = (l+r)//2
            while(l<=r):
                if row[mid] <target:
                    l = mid+1
                elif row[mid] > target:
                    r = mid -1
                else:
                    return True
                mid = (l+r)//2
            
        return False
                    
