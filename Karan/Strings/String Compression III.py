class Solution:
 def compressedString(self, word):
  comp = []
  i, n = 0, len(word)
  while i < n:
   count = 1
   while i + count < n and word[i] == word[i + count] and count < 9:
    count += 1
   comp.append(str(count) + word[i])
   i += count
  return "".join(comp)