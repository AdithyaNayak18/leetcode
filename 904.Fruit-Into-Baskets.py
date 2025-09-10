class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        m,l,r=0,0,0
        mydict=dict()
        while r<len(fruits):
            mydict[fruits[r]]=mydict.get(fruits[r],0)+1
            while len(mydict)>2:
                mydict[fruits[l]]-=1
                if mydict[fruits[l]]==0:
                    del mydict[fruits[l]]
                l+=1
            if len(mydict)<=2:
                m=max(m,r-l+1)
            r+=1
        return m
            
