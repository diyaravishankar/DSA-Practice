class Solution:
 def generate(self, numRows):
  triangle = []
  for i in range(numRows):
   if i == 0:
    triangle.append([1])
   else:
    row = [1]
    for j in range(1, i):
     row.append(triangle[i-1][j-1] + triangle[i-1][j])
    row.append(1)
    triangle.append(row)
  return triangle