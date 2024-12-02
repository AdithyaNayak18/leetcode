class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res=0
        s=0
        for i in gain:
            s+=i
            res=max(s,res)

        return res
