class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
        if len(nums)==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        else:
            return len(nums)-1
        
