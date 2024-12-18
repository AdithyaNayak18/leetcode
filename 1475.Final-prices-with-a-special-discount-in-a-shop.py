class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        dis=[p for p in prices]
        s=[]
        for i in range(len(prices)):
            while s and prices[s[-1]]>=prices[i]:
                ele=s.pop()
                dis[ele]-=prices[i]
            s.append(i)
        return dis
