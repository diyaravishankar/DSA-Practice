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