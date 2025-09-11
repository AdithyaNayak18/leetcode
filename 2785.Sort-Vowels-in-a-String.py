class Solution:
    def sortVowels(self, s: str) -> str:
        v=[]
        ns=s
        for i in range(0,len(s)):
            if s[i] in "AEIOUaeiou":
                v.append(s[i])
        
        v.sort()
        nv=''.join(v)
        #return nv
        j=0
        for i in range(0,len(s)):
            if s[i] in "AEIOUaeiou":
                ns=ns[:i]+nv[j]+ns[i+1:]
                j+=1
        return ns
