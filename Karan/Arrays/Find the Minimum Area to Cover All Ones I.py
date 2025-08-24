class Solution:
    def minAreaRect(self, grid: list[list[int]]) -> int:
        m,n=len(grid),len(grid[0])
        min_r,max_r,min_c,max_c=m,-1,n,-1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    min_r=min(min_r,i)
                    max_r=max(max_r,i)
                    min_c=min(min_c,j)
                    max_c=max(max_c,j)
        return (max_r-min_r+1)*(max_c-min_c+1)