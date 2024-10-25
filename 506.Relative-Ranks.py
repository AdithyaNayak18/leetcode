class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sc=sorted(score,reverse=True)
        count={}   #dictionary
        for i in range(len(sc)):
            if i==0:
                count[sc[i]]="Gold Medal"
            elif i==1:
                count[sc[i]]="Silver Medal"
            elif i==2:
                count[sc[i]]="Bronze Medal"
            else:
                count[sc[i]]=str(i+1)

        res=[]
        for i in score:
            res.append(count[i])

        return res



            

        
