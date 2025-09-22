class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        f=collections.Counter(nums)
        m=max(f.values())
        c=0
        for i in f.values():
            if i==m:
                c+=m
        return c
