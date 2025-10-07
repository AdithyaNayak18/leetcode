class Solution:
    def dfs(self,currnode,visited,graph,color):
        visited[currnode]=color
        for adjnode in graph[currnode]:
            if visited[adjnode]!=-1:
                if visited[adjnode]==color:
                    return False
            else:
                if color==0:
                    ans=self.dfs(adjnode,visited,graph,1)
                else:
                    ans=self.dfs(adjnode,visited,graph,0)
                if ans==False:
                    return False
        return True


    def isBipartite(self, graph: List[List[int]]) -> bool:
        totnodes=len(graph)
        visited=[-1]*totnodes
        for i in range(0,totnodes):
            if visited[i]==-1:
                ans=self.dfs(i,visited,graph,0)
                if ans==False:
                    return False
        return True
