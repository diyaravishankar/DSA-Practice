class Solution:
 def possibleStringCount(self, word: str) -> int:
  groups = []
  i = 0
  while i < len(word):
   j = i
   while j < len(word) and word[j] == word[i]:
    j += 1
   groups.append((word[i], j - i))
   i = j
  possible = set()
  possible.add(word)
  for idx, (ch, cnt) in enumerate(groups):
   if cnt == 1:
    continue
   for new_len in range(1, cnt):
    new_word = ''
    for i, (c, n) in enumerate(groups):
     if i == idx:
      new_word += c * new_len
     else:
      new_word += c * n
    possible.add(new_word)
  return len(possible)
