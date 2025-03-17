class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        os=set()
        for n in nums:
            if n not in os:
                os.add(n)
            else:
                os.remove(n)

        return len(os)==0
