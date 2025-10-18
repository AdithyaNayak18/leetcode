class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjlist=[[] for _ in range(n)]
        for u,v,cost  in flights:
            adjlist[u].append([v,cost])
        mincost=[sys.maxsize for _ in range(n)]
        mincost[src]=0
        queue=deque()
        queue.append([0,src,0])
        while len(queue)!=0:
            step,node,cost=queue.popleft()
            for adjnode,price in adjlist[node]:
                nc=cost+price
                if nc<mincost[adjnode]:
                    ns=step+1
                    if ns==k+1:
                        if adjnode!=dst:
                            continue 
                    mincost[adjnode]=nc
                    queue.append([ns,adjnode,nc])
        if mincost[dst]==sys.maxsize:
            return -1
        return mincost[dst]
