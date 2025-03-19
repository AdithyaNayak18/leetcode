class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations=[[]]
        for n in nums:
            newp=[]
            for p in permutations:
                for i in range(len(p)+1):
                    np=p.copy()
                    np.insert(i,n)
                    newp.append(np)
            permutations=newp
        return permutations
