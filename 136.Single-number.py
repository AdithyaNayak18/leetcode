#Brute Force
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l=list(nums)
        for i in range(len(l)):
            if l.count(l[i])==1:
                return l[i]

        return None
        
#OPTIMAL - Bit Manipulation
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for n in nums:
            res=res^n
        return res
