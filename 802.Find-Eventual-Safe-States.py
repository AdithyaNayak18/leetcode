class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        v = len(graph)
        adjlist=[[] for _ in range(v)]
        for node in range(v):
            for adjnode in graph[node]:
                adjlist[adjnode].append(node)

        queue=deque()

        indegree=[0 for _ in range(v)]
        for node in range(len(adjlist)):
            for adjnode in adjlist[node]:
                indegree[adjnode]+=1

        for node in range(0,v):
            if indegree[node]==0:
                queue.append(node)

        res=[]
        while len(queue)!=0:
            node=queue.popleft()
            res.append(node)
            for adjnode in adjlist[node]:
                indegree[adjnode]-=1
                if indegree[adjnode]==0:
                    queue.append(adjnode)
        res.sort()
        return res
