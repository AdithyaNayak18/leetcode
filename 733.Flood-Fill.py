class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i,j,color,initialcolor,vis,r,c):
            if i<0 or i>=r or j<0 or j>=c:
                return
            if vis[i][j]!=initialcolor:
                return
            if vis[i][j]==color:
                return
            vis[i][j]=color
            dfs(i+1,j,color,initialcolor,vis,r,c)
            dfs(i,j-1,color,initialcolor,vis,r,c)
            dfs(i-1,j,color,initialcolor,vis,r,c)
            dfs(i,j+1,color,initialcolor,vis,r,c)
        if image[sr][sc]==color:
            return image
        vis=deepcopy(image)
        r,c=len(vis),len(vis[0])
        initialcolor=vis[sr][sc]
        dfs(sr,sc,color,initialcolor,vis,r,c)
        return vis
