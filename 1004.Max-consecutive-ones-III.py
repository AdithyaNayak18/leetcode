class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r,m=0,0,0
        z=0
        n=len(nums)
        while r<n:
            if nums[r]==0:
                z+=1
            while z>k:
                if nums[l]==0:
                    z-=1
                l+=1
            if z<=k:
                m=max(m,r-l+1)
            r+=1
        return m
            
