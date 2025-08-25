class Solution:
    def find132pattern(self, nums):
        stack=[]
        s3=float('-inf')
        for num in reversed(nums):
            if num<s3:
                return True
            while stack and num>stack[-1]:
                s3=stack.pop()
            stack.append(num)
        return False