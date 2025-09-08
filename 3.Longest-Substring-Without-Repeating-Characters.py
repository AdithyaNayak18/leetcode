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


#Optimal using dictionary
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap=dict()
        l,r=0,0 #left,right
        length=0
        n=len(s)
        while r<n:
            if s[r] in hashmap:
                l=max(hashmap[s[r]]+1,l)
            hashmap[s[r]]=r
            length=max(length,r-l+1)
            r+=1
        return length


