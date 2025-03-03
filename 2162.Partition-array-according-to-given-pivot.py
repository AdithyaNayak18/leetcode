class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arr=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                arr.append(nums[i])
        
        for i in range(len(nums)):
            if nums[i]==pivot:
                arr.append(nums[i])

        for i in range(len(nums)):
            if nums[i]>pivot:
                arr.append(nums[i])

        return arr
