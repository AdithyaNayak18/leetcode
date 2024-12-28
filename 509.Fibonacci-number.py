class Solution:
    def fib(self, n: int) -> int:
        def fsum(num):
            if num<=1:
                return num

            return fsum(num-1)+fsum(num-2)
        
        res=fsum(n)
        return res
