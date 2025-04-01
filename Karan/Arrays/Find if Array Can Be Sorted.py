class Solution:
 def compressedString(self, word: str) -> str:
  comp=""
  i=0
  while i<len(word):
   count=1
   while i+1<len(word) and word[i]==word[i+1] and count<9:
    count+=1
    i+=1
   comp+=str(count)+word[i]
   i+=1
  return comp

 def canSortArray(self, nums: list[int]) -> bool:
  def count_set_bits(x):
   return bin(x).count("1")
  n=len(nums)
  i=0
  while i<n:
   j=i
   while j+1<n and count_set_bits(nums[j])==count_set_bits(nums[j+1]):
    j+=1
   nums[i:j+1]=sorted(nums[i:j+1])
   i=j+1
  return nums==sorted(nums)