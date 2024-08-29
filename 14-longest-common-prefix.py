class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        st=""
        for i in range(len(strs[0])):
            for s in strs:
                if i==len(s) or s[i]!=strs[0][i]: #comparing a subset it to the first string
                    return st

            st+=strs[0][i]
        
        return st
