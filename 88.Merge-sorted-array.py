class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1.sort()
        index=0 
        if n>0:
            for i in range(0,len(nums1)):
                if nums1[i]==0:
                    nums1[i]=nums2[index]
                    index+=1 
                    if index==n:
                        break
        nums1.sort()
        return nums1