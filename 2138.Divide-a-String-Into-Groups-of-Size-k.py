class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n=len(s)
        if n%k!=0:
            r=n%k
            for i in range(0,k-r):
                s+=fill
                    
        n=len(s)
        cs=""
        fs=[]
        for i in range(0,n,k):
            cs=s[i:i+k]
            fs.append(cs)
            cs=""
        return fs
            
