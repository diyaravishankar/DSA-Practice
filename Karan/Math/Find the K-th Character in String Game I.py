class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            next_part = ""
            for c in word:
                next_char = chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
                next_part += next_char
            word += next_part
        return word[k - 1]