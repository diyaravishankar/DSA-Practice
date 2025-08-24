class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        def dfs(nums):
            if len(nums)==1:
                return abs(nums[0]-24)<1e-6
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i!=j:
                        nxt=[]
                        for k in range(len(nums)):
                            if k!=i and k!=j:
                                nxt.append(nums[k])
                        for val in calc(nums[i],nums[j]):
                            if dfs(nxt+[val]):
                                return True
            return False
        def calc(a,b):
            res=[a+b,a-b,b-a,a*b]
            if abs(b)>1e-6: res.append(a/b)
            if abs(a)>1e-6: res.append(b/a)
            return res
        return dfs([float(x) for x in cards])