class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m,s=0,0
        zero=-1
        for i in range(len(nums)):
            if nums[i]==0:
                s=zero+1
                zero=i
            m=max(m,i-s)            
        return m
