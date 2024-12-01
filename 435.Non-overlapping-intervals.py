class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        c=0
        pe=intervals[0][1]
        for s,e in intervals[1:]:
            if s>=pe:
                pe=e
            else:
                c+=1
                pe=min(e,pe)
        return c
