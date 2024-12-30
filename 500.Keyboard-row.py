class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res=[]
        r1 = set('qwertyuiop')
        r2 = set('asdfghjkl')
        r3 = set('zxcvbnm')
        for word in words:
            w=set(word.lower())
            if w<=r1 or w<=r2 or w<=r3 :
                res.append(word)
        return res
