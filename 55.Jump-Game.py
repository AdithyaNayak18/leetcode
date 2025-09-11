class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxindex=0
        for i in range(0,len(nums)):
            if i>maxindex:
                return False
            
            maxindex=max(maxindex,i+nums[i])
        return True
