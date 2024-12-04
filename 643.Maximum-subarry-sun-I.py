class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        csum=0
        
        for i in range(k):
            csum+=nums[i]
        
        mavg=csum/k

        for i in range(k,len(nums)):
            csum+=nums[i]
            csum-=nums[i-k]
            avg=csum/k
            mavg=max(mavg,avg)
        
        return mavg
