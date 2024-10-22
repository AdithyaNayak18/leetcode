class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[1]
        for i in range(rowIndex):
            nrow = [0]*(len(res)+1)
            for j in range(len(res)):
                nrow[j]+=res[j]
                nrow[j+1]+=res[j]
            res=nrow

        return res
        



        
