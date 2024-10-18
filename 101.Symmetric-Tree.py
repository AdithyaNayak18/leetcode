# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(lp,rp):
            if not lp and not rp:
                return True

            if not lp or not rp:
                return False

            return(lp.val == rp.val and
            dfs(lp.left,rp.right) and dfs(lp.right,rp.left))

        
        return dfs(root.left,root.right)
        
