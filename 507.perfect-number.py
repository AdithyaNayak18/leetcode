class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        s=0
        for i in range(1,int(num**0.5)+1):
            if num%i==0:
                s+=i
                if i*i != num:
                    s+=num//i
        return s-num==num
