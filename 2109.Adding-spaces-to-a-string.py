class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i,j=0,0
        res=""
        while i<len(s) and j<len(spaces):
            if i<spaces[j]:
                res+=s[i]
                i+=1
            else:
                res+=" "
                j+=1

        if i<len(s):
            res+=s[i:]
        return res
