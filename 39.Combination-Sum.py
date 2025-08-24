class Solution:
    def backtrack(self,i,tot,sub,cand,target,res):
        if tot==target:
            res.append(sub.copy())
            return
        elif tot>target:
            return        
        if i>=len(cand):
            return
        

        Sum=tot+cand[i]
        sub.append(cand[i])
        self.backtrack(i,Sum,sub,cand,target,res)
        Sum=tot
        sub.pop()
        self.backtrack(i+1,Sum,sub,cand,target,res)


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        self.backtrack(0,0,[],candidates,target,res)
        return res
