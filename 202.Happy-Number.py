class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()
        while n not in visit:
            visit.add(n)
            n=self.sumofsq(n)
            if n==1:
                return True
        return False


    def sumofsq(self,n:int)->int:
        o=0
        while n:
            d=n%10
            d=d**2
            o+=d
            n=n//10
        return o
