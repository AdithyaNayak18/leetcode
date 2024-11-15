class Solution:
    def tribonacci(self, n: int) -> int:
        t=[0,1,1]
        for i in range(3,n+1):
            curr=t[i-1]+t[i-2]+t[i-3]
            t.append(curr)
        
        return t[n]
