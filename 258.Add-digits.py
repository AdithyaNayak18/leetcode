class Solution:
    def addDigits(self, num: int) -> int:
        n = str(num)
        
        while len(n)!=1:
            sum=0
            for i in n:
                sum+=int(i)
            n=str(sum)
        
        return int(n)
