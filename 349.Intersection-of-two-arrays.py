class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a1=set(nums1)
        res=[]
        for i in nums2:
            if i in a1:
                res.append(i)
                a1.remove(i)
        return res
