class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        l=defaultdict(int)
        r=Counter(nums)

        for i in range(len(nums)):
            l[nums[i]]+=1
            r[nums[i]]-=1

            leftlen=i+1
            rightlen=len(nums)-i-1 
            if 2*l[nums[i]]>leftlen and 2*r[nums[i]]>rightlen:
                return i

        return -1
