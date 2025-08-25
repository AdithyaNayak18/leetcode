class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        n=len(candidates)
        def backtrack(i,curr,total):
            if total==target:
                res.append(curr.copy())
                return
            if total>target or i==n:
                return
            
            curr.append(candidates[i])
            backtrack(i+1,curr,total+candidates[i])
            curr.pop()
            while i+1<n and candidates[i]==candidates[i+1]:
                i+=1
            backtrack(i+1,curr,total)
        
        backtrack(0,[],0)
        return res
