class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        for r in grid:
            for c in r:
                if c%x!=grid[0][0]%x:
                    return -1

        nums=[n for r in grid for n in r]
        nums.sort()

        p=0
        t=sum(nums)
        res=float("inf")
        for i in range(len(nums)):
            cl=nums[i]*i - p
            cr=t-p-(nums[i]*(len(nums)-i))
            op=(cl+cr)//x
            res=min(res,op)
            p+=nums[i]

        return res
