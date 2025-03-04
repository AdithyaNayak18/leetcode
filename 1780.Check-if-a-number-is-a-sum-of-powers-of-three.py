class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        i=0
        while 3**(i+1)<=n:
            i+=1

        while i>=0:
            p=3**i
            if p<=n:
                n-=p
            i-=1
        
        return n==0
