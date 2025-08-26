class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        n=len(dimensions)
        ld,ba=-1,-1
        for w,h in dimensions:
            d = w*w + h*h
            if d>ld:
                ld=d
                ba=w*h
            elif d==ld and ba<w*h:
                ba=w*h
        return ba
