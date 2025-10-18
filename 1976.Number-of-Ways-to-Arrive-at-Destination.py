class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD=10**9+7
        adjlist=[[] for _ in range(n)]
        for u,v,w in roads:
            adjlist[u].append([v,w])
            adjlist[v].append([u,w])
        
        distance=[sys.maxsize for _ in range(n)]
        ways=[0 for _ in range(n)]
        distance[0]=0
        ways[0]=1
        pq=[[0,0]]
        while len(pq)!=0:
            dist,node=heapq.heappop(pq)
            for adjnode,weight in adjlist[node]:
                newdist=dist+weight
                if newdist<distance[adjnode]:
                    distance[adjnode]=newdist
                    heapq.heappush(pq,[newdist,adjnode])
                    ways[adjnode]=ways[node]
                elif newdist==distance[adjnode]:
                    ways[adjnode]+=ways[node]
        return ways[n-1]%MOD
            
