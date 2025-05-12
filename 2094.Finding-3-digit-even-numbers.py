class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq=Counter(digits)
        res=[]
        for i in range(100,1000,2):
            d1=i//100
            d2=(i//10)%10
            d3=i%10
            cf=Counter([d1,d2,d3])
            if all(freq[d]>=cf[d] for d in cf):
                res.append(i)

        return res
