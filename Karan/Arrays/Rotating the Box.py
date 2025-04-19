class Solution:
 def rotateTheBox(self, boxGrid):
  m=len(boxGrid)
  n=len(boxGrid[0])
  for i in range(m):
   k=n-1
   for j in range(n-1,-1,-1):
    if boxGrid[i][j]=='*':
     k=j-1
    elif boxGrid[i][j]=='#':
     boxGrid[i][j]='.'
     boxGrid[i][k]='#'
     k-=1
  res=[[None]*m for _ in range(n)]
  for i in range(m):
   for j in range(n):
    res[j][m-1-i]=boxGrid[i][j]
  return res