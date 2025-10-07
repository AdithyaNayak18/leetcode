class Solution:
    def dfs(self,r,c,rows,cols,grid,visited):
        if r<0 or c<0 or r>rows-1 or c>cols-1:
            return
        if grid[r][c]=="0":
            return
        if visited[r][c]==1:
            return
        visited[r][c]=1
        self.dfs(r-1,c,rows,cols,grid,visited)
        self.dfs(r,c-1,rows,cols,grid,visited)
        self.dfs(r+1,c,rows,cols,grid,visited)
        self.dfs(r,c+1,rows,cols,grid,visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        cnt=0
        rows=len(grid)
        cols=len(grid[0])
        visited=[[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and visited[r][c]==0:
                    cnt+=1
                    self.dfs(r,c,rows,cols,grid,visited)
        return cnt
        
