class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        tot,c=0,0
        res=[]
        def backtrack(idx,tot,sub):
            if tot==n and len(sub)==k:
                res.append(sub.copy())
                return
            if tot>n or len(sub)>k:
                return

            for i in range(idx,10):
                sum=tot+i
                sub.append(i)
                backtrack(i+1,sum,sub)
                sub.pop()
        
        backtrack(1,0,[])
        return res
