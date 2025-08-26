from bisect import bisect_right, insort
class Solution:
    def resultArray(self, nums):
        arr1, arr2 = [nums[0]], [nums[1]]
        s1, s2 = [nums[0]], [nums[1]]
        for i in range(2, len(nums)):
            x = nums[i]
            g1 = len(s1) - bisect_right(s1, x)
            g2 = len(s2) - bisect_right(s2, x)
            if g1 > g2:
                arr1.append(x)
                insort(s1, x)
            elif g1 < g2:
                arr2.append(x)
                insort(s2, x)
            else:
                if len(arr1) <= len(arr2):
                    arr1.append(x)
                    insort(s1, x)
                else:
                    arr2.append(x)
                    insort(s2, x)
        return arr1 + arr2