class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr=[a-b for a,b in zip(nums1,nums2)]
        def merge_sort(l,r):
            if l>=r:
                return 0
            m=(l+r)//2
            cnt=merge_sort(l,m)+merge_sort(m+1,r)
            j=m+1
            for i in range(l,m+1):
                while j<=r and arr[j]<arr[i]-diff:
                    j+=1
                cnt+=r-j+1
            arr[l:r+1]=sorted(arr[l:r+1])
            return cnt
        return merge_sort(0,len(arr)-1)