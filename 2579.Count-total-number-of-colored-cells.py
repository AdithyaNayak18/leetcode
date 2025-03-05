class Solution:
    def coloredCells(self, n: int) -> int:
        if n==0:
            return 0
        c=1
        for i in range(2,n+1):
            c=c+(4*(i-1))
        return c
