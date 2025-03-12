class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        nc,pc=0,0
        for i in range(len(nums)):
            if nums[i]<0:
                nc+=1
            elif nums[i]==0:
                continue
            else:
                pc+=1
        
        return max(nc,pc)
