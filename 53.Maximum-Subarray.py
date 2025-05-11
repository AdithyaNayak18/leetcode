class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Maxsub=nums[0]
        cs=0
        for n in nums:
            if cs<0:
                cs=0
            cs+=n
            Maxsub=max(Maxsub,cs)
        return Maxsub
