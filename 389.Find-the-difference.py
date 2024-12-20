class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ss,ts=0,0
        for c in s:
            ss+=ord(c)
        for c in t:
            ts+=ord(c)
        return chr(ts-ss)
