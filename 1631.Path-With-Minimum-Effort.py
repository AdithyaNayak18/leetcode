class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row=len(heights)
        cols=len(heights[0])
        effort_arr=[[sys.maxsize for _ in range(cols)] for _ in range(row)]
        effort_arr[0][0]=0
        priority_queue=[[0,0,0]]
        while len(priority_queue)!=0:
            eff,i,j=heapq.heappop(priority_queue)
            if i==row-1 and j==cols-1:
                return eff
            for x,y in [[-1,0],[0,-1],[0,1],[1,0]]:
                newi,newj=i+x,j+y
                if newi<0 or newj<0 or newi>=row or newj>=cols:
                    continue
                neweff=max(abs(heights[newi][newj]-heights[i][j]),eff)
                if neweff<effort_arr[newi][newj]:
                    effort_arr[newi][newj]=neweff
                    heapq.heappush(priority_queue,[neweff,newi,newj])


                
