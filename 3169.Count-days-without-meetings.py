class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        pe=0
        for s,e in meetings:
            s=max(s,pe+1)
            length=e-s+1
            days-=max(length,0)
            pe=max(pe,e)

        return days
