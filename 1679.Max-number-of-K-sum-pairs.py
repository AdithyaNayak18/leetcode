class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l,r=0,len(nums)-1
        nums.sort()
        c=0
        while(l<r):
            if nums[l]+nums[r]==k:
                c+=1
                # nums.pop(l)
                # nums.pop(r)
                l+=1
                r-=1
            elif nums[l]+nums[r]<k:
                l+=1
            else:
                r-=1

        return c
        
