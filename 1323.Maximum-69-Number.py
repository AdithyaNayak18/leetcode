class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        if not "6" in s:
            return num
        
        i = s.index("6")
        return int(s[:i] + "9" + s[i+1:])
