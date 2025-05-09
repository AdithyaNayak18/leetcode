class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern)!=len(words):
            return False
        
        ltow={}
        wtol={}
        for l,w in zip(pattern,words):
            if l in ltow and ltow[l]!=w:
                return False
            if w in wtol and wtol[w]!=l:
                return False
            ltow[l]=w
            wtol[w]=l

        return True
