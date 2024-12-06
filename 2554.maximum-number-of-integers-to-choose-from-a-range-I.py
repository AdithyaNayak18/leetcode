class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        s,c=0,0
        banned=set(banned)
        for i in range(1,n+1):
            if i not in banned:
                if s+i>maxSum:
                    return c
                s+=i
                c+=1
        return c
    
