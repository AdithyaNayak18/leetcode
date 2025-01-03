class Solution:
    def countBits(self, n: int) -> List[int]:
        def decimalToBinary(n): 
            return bin(n).replace("0b", "") 
        res=[]
        for i in range(n+1):
            n=0
            b=decimalToBinary(i)
            b=str(b)
            for c in b:
                if c=='1':
                    n+=1
            
            res.append(n)
        return res
