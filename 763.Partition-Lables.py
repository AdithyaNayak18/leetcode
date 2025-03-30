class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex={}
        for i,c in enumerate(s):  #i->index,c->character
            lastindex[c]=i
        res=[]
        size,e=0,0
        for i,c in enumerate(s):
            size+=1
            if lastindex[c]>e:
                e=lastindex[c]
            
            if i==e:
                res.append(size)
                size=0
        
        return res    
