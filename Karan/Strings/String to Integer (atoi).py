class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:] 
        elif s[0] == '+':
            s = s[1:]
        result = 0
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)
        result *= sign
        int_min = -2**31
        int_max = 2**31 - 1
        if result < int_min:
            return int_min
        if result > int_max:
            return int_max
        return result