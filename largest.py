class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        for i in range (1,m):
            for j in range(n):
                if matrix[i][j]==1:
                    matrix[i][j]+=matrix[i-1][j]
        ans=0
        for row in matrix:
            sorted_row=sorted(row,reverse=True)
            for i in range (n ):
                area=sorted_row[i]*(i+1)
                ans=max(ans,area)
        return ans
