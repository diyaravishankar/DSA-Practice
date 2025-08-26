class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n=len(nums)
        pos={v:i for i,v in enumerate(nums)}
        arr=sorted(nums)
        ans=n
        for i in range(1,n):
            if pos[arr[i]]<pos[arr[i-1]]:
                ans+=n-i
        return ans