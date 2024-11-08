class Solution:
    def countAndSay(self, n: int) -> str:
        def ans(s):
            res=""
            c=1
            for i in range(len(s)):
                if i==len(s)-1 or s[i]!=s[i+1]:
                    res+=str(c)+s[i]
                    c=1
                else:
                    c+=1
            return res

        answer="1"
        for i in range(2,n+1):
            answer=ans(answer)
        return answer

