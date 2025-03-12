class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l,rc=0,0
        res=k
        for i in range(len(blocks)):
            if blocks[i]=='W':
                rc+=1
            if i-l+1==k:
                res=min(res,rc)
                if blocks[l]=="W":
                    rc-=1
                l+=1
        return res
