class Solution:
 def vowelStrings(self, words, queries):
  vowels={'a','e','i','o','u'}
  def is_vowel_word(w):
   return w[0] in vowels and w[-1] in vowels
  n=len(words)
  prefix=[0]*(n+1)
  for i in range(n):
   prefix[i+1]=prefix[i]+(1 if is_vowel_word(words[i]) else 0)
  return [prefix[r+1]-prefix[l] for l,r in queries]