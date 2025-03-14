class Solution:
 def maximumSwap(self,num:int)->int:
  num_str=list(str(num))
  last={int(d):i for i,d in enumerate(num_str)}
  for i,d in enumerate(num_str):
   for bigger in range(9,int(d),-1):
    if bigger in last and last[bigger]>i:
     num_str[i],num_str[last[bigger]]=num_str[last[bigger]],num_str[i]
     return int("".join(num_str))
  return num