class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        edges=prerequisites
        adjlist=[[] for _ in range(numCourses)]
        indegree=[0 for _ in range(numCourses)]
        for u,v in edges:
            adjlist[u].append(v)
            indegree[v]+=1

        queue=deque()
        res=[]
        for i in range(0,numCourses):
            if indegree[i]==0:
                queue.append(i)
        
        while len(queue)!=0:
            currnode=queue.popleft()
            res.append(currnode)
            for adjnode in adjlist[currnode]:
                indegree[adjnode]-=1
                if indegree[adjnode]==0:
                    queue.append(adjnode)
        if len(res)==numCourses:
            return True
        return False
