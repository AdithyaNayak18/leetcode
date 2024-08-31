class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        
        for i in range(len(haystack)+1-len(needle)): #so that we dont hae to check the haystack if size ofremaininghaystackislessthanthatof needle
            for j in range(len(needle)):
                if haystack[i+j]!=needle[j]:
                    break
                if j==len(needle)-1:
                    return i
        return -1

