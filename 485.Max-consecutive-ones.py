class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m,c=0,0
        for i in range(len(nums)):
            
            if nums[i]==1:
                c+=1
            else:
                c=0
            if c>m:
                m=c
        return m
            
