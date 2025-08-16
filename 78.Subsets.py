#Greedy solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sub=[]
        def dfs(i):
            if i>=len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(i+1)

            sub.pop()
            dfs(i+1)
        dfs(0)
        return res


#Bit Manipulation Solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        ts=1<<n
        for num in range(0,ts):
            lst=[]
            for i in range(0,n):
                if num&(1<<i)!=0:
                    lst.append(nums[i])
            res.append(lst)
        return res
