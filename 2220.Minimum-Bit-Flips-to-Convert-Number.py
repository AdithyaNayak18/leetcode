class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        n=start^goal
        c=0
        for i in range(0,32):
            if n&(1<<i)!=0:
                c+=1
        return c
