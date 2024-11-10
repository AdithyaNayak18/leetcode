class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n=len(candies)
        res=[False]*n
        m=max(candies)
        for i in range(n):
            if candies[i]+extraCandies>=m:
                res[i]=True
                
        return res
