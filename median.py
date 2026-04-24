import bisect

class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        low = 1
        high = 2000
        desired = (n * m) // 2
        
        while low < high:
            mid = (low + high) // 2
            count = 0
            
            for row in mat:
                count += bisect.bisect_right(row, mid)
            
            if count <= desired:
                low = mid + 1
            else:
                high = mid
        
        return low
