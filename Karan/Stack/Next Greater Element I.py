class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack=[]
        nge={}
        for num in nums2:
            while stack and num>stack[-1]:
                nge[stack.pop()]=num
            stack.append(num)
        while stack:
            nge[stack.pop()]=-1
        return [nge[num] for num in nums1]