class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k==0:
            return 1.0
        
        wsum=0
        for i in range(k,k+maxPts):
            wsum+=1 if i<=n else 0
        
        dp={}#cache(Hashmap) to read prev values
        for i in range(k-1,-1,-1):
            dp[i] = wsum/maxPts
            remove=0
            if i + maxPts <= n:
                remove = dp.get(i+maxPts,1)
            wsum += dp[i] - remove
        return dp[0]
