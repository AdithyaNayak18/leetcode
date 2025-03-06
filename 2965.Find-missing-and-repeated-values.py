class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N=len(grid)
        c=defaultdict(int)

        for i in range(N):
            for j in range(N):
                c[grid[i][j]]+=1

        a,b=0,0

        for num in range(1,N*N+1):
            if c[num]==0:
                a=num
            if c[num]==2:
                b=num
        
        return [b,a]
