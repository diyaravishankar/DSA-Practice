class Solution:
 def uniquePathsWithObstacles(self, grid):
  m=len(grid)
  n=len(grid[0])
  if grid[0][0]==1 or grid[m-1][n-1]==1:
   return 0
  dp=[[0]*n for _ in range(m)]
  dp[0][0]=1
  for i in range(m):
   for j in range(n):
    if grid[i][j]==1:
     dp[i][j]=0
    elif i==0 and j==0:
     continue
    else:
     up=dp[i-1][j] if i>0 else 0
     left=dp[i][j-1] if j>0 else 0
     dp[i][j]=up+left
  return dp[m-1][n-1]