class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        
        rows=len(grid)
        cols=len(grid[0])
        dist=[[sys.maxsize for _ in range(cols)] for _ in range(rows)]
        dist[0][0]=1
        q=deque()
        q.append([1,0,0])
        while len(q)!=0:
            d,i,j=q.popleft()
            for x,y in [[1,0],[0,-1],[-1,0],[0,1],[-1,-1],[-1,1],[1,1],[1,-1]]:
                newi,newj=i+x,j+y
                if newi<0 or newj<0 or newi>=rows or newj>=cols:
                    continue
                if grid[newi][newj]==1:
                    continue
                dist_trav=d+1
                if dist_trav<dist[newi][newj]:
                    dist[newi][newj]=dist_trav
                    q.append([dist_trav,newi,newj])
            
        
        if dist[rows-1][cols-1]==sys.maxsize:
            return -1
        
        return dist[rows-1][cols-1]
