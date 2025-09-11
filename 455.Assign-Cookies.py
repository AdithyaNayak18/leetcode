class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gp,sp=0,0
        gl,sl=len(g),len(s)
        i,j,c=0,0,0
        while i<gl and j<sl:
            if g[i]<=s[j]:
                c+=1
                i+=1
            j+=1
                    
        return c
        
