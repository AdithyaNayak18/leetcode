class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res=0
        l,curr=0,0
        for r in range(len(nums)):
            while curr & nums[r]:
                curr=curr^nums[l]
                l+=1
            res=max(res,r-l+1)
            curr=curr | nums[r]
        return res
