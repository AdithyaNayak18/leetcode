class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        pm=nums[0]
        md,res=0,0
        for i in range(1,len(nums)):
            res=max(res,md*nums[i])
            pm=max(pm,nums[i])
            md=max(md,pm-nums[i])

        return res
