class Solution:
    def findLucky(self, arr: List[int]) -> int:
        s=Counter(arr)
        m=-1
        for c in s:
            if s[int(c)]==int(c):
                if c>m:
                    m=c
        return m
