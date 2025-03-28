class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        row,col=len(grid),len(grid[0])
        q=[(n,i)for i,n in enumerate(queries)]
        q.sort()

        minheap=[(grid[0][0] , 0,0)]
        visit=set([(0,0)])
        res = [0]*len(queries)
        p=0

        for limit,index in q:
            while minheap and minheap[0][0] < limit:
                val,r,c=heappop(minheap)
                p+=1
                neighbours=[[r+1,c] , [r-1 , c] , [r,c+1] , [r,c-1]]
                for nr,nc in neighbours:
                    if(
                        0 <= nr < row  and 0 <= nc < col and
                        (nr,nc) not in visit
                    ):
                        heappush(minheap, (grid[nr][nc] ,nr,nc))
                        visit.add((nr,nc))
                        
            res[index]=p
        return res
