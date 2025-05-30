class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s==" ":
            return True
        s = ''.join([char for char in s if char.isalnum()])
        s=s.lower()
        b,e=0,len(s)-1
        while b<=e:
            if s[b]==s[e]:
                b+=1
                e-=1
                continue
            else:
                return False
        return True
