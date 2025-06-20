class Solution:
 def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
  if not set(s2).issubset(set(s1)):
   return 0
  index = 0
  count1 = count2 = 0
  lookup = {}
  while count1 < n1:
   for ch in s1:
    if ch == s2[index]:
     index += 1
     if index == len(s2):
      count2 += 1
      index = 0
   count1 += 1
   key = (index,)
   if key in lookup:
    prev_count1, prev_count2 = lookup[key]
    cycle_len = count1 - prev_count1
    cycle_cnt2 = count2 - prev_count2
    remaining = n1 - count1
    cycles = remaining // cycle_len
    count1 += cycles * cycle_len
    count2 += cycles * cycle_cnt2
   else:
    lookup[key] = (count1, count2)
  return count2 // n2