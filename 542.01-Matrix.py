from collections import deque
from copy import deepcopy
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows=len(mat)
        cols=len(mat[0])
        vis=[[0 for _ in range(cols)] for _ in range(rows)]
        dist=[[0 for _ in range(cols)] for _ in range(rows)]
        queue=deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c]==0:
                    queue.append([r,c,0])
                    vis[r][c]=1
        while len(queue)!=0:
            i,j,d=queue.popleft()
            dist[i][j]=d
            for x,y in [(-1,0),(0,-1),(0,1),(1,0)]:
                newi,newj=i+x,j+y
                if newi<0 or newi>r or newj<0 or newj>c:
                    continue
                if vis[newi][newj]==1:
                    continue
                queue.append([newi,newj,d+1])
                vis[newi][newj]=1
        return dist
