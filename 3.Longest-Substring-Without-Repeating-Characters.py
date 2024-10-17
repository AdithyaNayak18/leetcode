class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()
        left=0
        result=0
        for c in range(len(s)):
            while s[c] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[c])
            result=max(result,c-left+1)

        return result
