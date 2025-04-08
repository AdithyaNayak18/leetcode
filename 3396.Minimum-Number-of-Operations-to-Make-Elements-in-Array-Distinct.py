class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d=deque((nums))
        map=defaultdict(int)
        for x in d : map[x]+=1
        c=0

        while True:
            next=False
            for k in map:
                if map[k]>1:
                    next=True
                    break
            if not next: return c

            for i in range(3):
                curr=d.popleft()
                if not d : return c+1
                map[curr]-=1
            c+=1
