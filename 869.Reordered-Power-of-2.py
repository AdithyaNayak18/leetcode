class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def f(x):
            return "".join(sorted(str(x)))


        p=set()
        for i in range(32):
            num=pow(2,i)
            p.add(f(num))

        return f(n) in p
