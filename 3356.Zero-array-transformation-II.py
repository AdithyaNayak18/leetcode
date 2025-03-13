class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N=len(nums)
        Q=len(queries)
        def good(target):
            f=[0]*(N+1)
            for s,e,v in queries[:target]:
                f[s]+=v
                f[e+1]-=v

            for i in range(1,N+1):
                f[i]+=f[i-1]
            
            for i in range(N):
                if nums[i]>f[i]:
                    return False
            return True

        left=0
        right=Q+1

        while left<right:
            mid=(left+right)//2
            if good(mid):
                right=mid
            else:
                left=mid+1
        
        if left==Q+1:
            return -1
        return left
