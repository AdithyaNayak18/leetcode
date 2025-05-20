class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n=len(nums)
        d=[0]*(n+1)
        for l,r in queries:
            d[l]+=1
            d[r+1]-=1
        
        for i in range(1,n+1):
            d[i]+=d[i-1]

        for i in range(n):
            if nums[i]>d[i]:
                return False
        return True
